import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import ast

from analysis.helpers import constants as a_consts
from analysis.blocks import position as position_block
from analysis.blocks import scope as scope_block
from analysis.blocks import types as types_block
from analysis.blocks import variable as variable_block
from analysis.parsers import parser
from utils import cache


class VariableVisitor(parser.Traveller):
  def __init__(self, file_path):
    parser.Traveller.__init__(self)
    self.file_path = file_path
    scope = scope_block.Scope(a_consts.ROOT_SCOPE, None)
    self._current_scope = scope
    # Map: Key = Scope, Value = Map<VarName, Var>
    self.scope_variable_map = {
      scope: {}
    }
    # Map: Key = Name, Value = Scope
    self.scopes = {
      str(scope): scope
    }
    self.method_scopes = {a_consts.ROOT_SCOPE: str(scope)}

  def to_bson(self):
    d = {'file_path': self.file_path}
    if self.scopes:
      d['scopes'] = {}
      for key, val in self.scopes.items():
        d['scopes'][key] = val.to_bson()
    if self.scope_variable_map:
      d['scope_variable_map'] = {}
      for scope, variable_map in self.scope_variable_map.items():
        var_map = {}
        for var_name, variable in variable_map.items():
          var_map[var_name] = variable.to_bson()
        d['scope_variable_map'][str(scope)] = var_map
    if self.method_scopes:
      d['method_scopes'] = self.method_scopes
    return d

  @staticmethod
  def from_bson(bson_dict):
    o = VariableVisitor(bson_dict['file_path'])
    if 'scopes' in bson_dict:
      o.scopes = scope_block.from_bson(bson_dict['scopes'])
    if 'scope_variable_map' in bson_dict:
      o.scope_variable_map = {}
      for scope_str, var_map in bson_dict['scope_variable_map'].items():
        scope = o.scopes[scope_str]
        variables_map = {}
        for var_name, var_dict in var_map.items():
          variable = variable_block.Variable.from_json(var_dict, scope)
          variables_map[var_name] = variable
        o.scope_variable_map[scope] = variables_map
    if 'method_scopes' in bson_dict:
      o.method_scopes = bson_dict['method_scopes']
    return o

  @staticmethod
  def _is_variable_store(node):
    return types_block.BasicType.get_name(node.ctx) == "Store"

  def create_scope(self, name):
    scope = scope_block.Scope(name, self._current_scope)
    self.scopes[str(scope)] = scope
    self.scope_variable_map[scope] = {}
    self._current_scope.children[name] = scope
    self._current_scope = scope
    if name in self.method_scopes:
      raise RuntimeError("Method %s already")
    self.method_scopes[name] = str(scope)
    return scope

  def get_scope(self, scope_name):
    return self.scopes.get(scope_name, None)

  def list_variables(self):
    variables = []
    for variables_map in self.scope_variable_map.values():
      for scope_variables in variables_map.items():
        variables += scope_variables
    return variables

  def find_variable(self, variable_name, scope):
    curr_scope = scope
    while curr_scope and curr_scope in self.scope_variable_map:
      if variable_name in self.scope_variable_map[curr_scope]:
        return self.scope_variable_map[curr_scope][variable_name]
      curr_scope = curr_scope.parent
    return None

  def add_variable(self, name, position, var_type):
    variable_map = self.scope_variable_map.get(self._current_scope, {})
    variable = variable_block.Variable(name=name, scope=self._current_scope, var_type=var_type, positions={position})
    variable_map[name] = variable
    self.scope_variable_map[self._current_scope] = variable_map

  def update_variable(self, name, scope, position):
    variable = self.scope_variable_map.get(scope, {}).get(name, None)
    if not variable:
      raise RuntimeError("Variable with name '%s' not found in scope '%s'" % (name, scope.name))
    variable.positions.add(position)

  def visit_Name(self, node, meta):
    variable_name = node.id
    variable = self.find_variable(variable_name, self._current_scope)
    is_variable_store = VariableVisitor._is_variable_store(node)
    position = position_block.Position.get_position(node)
    if not variable and not is_variable_store:
      # Might be loading a global variable
      self._current_scope.update_dangling(variable_name, position)
      return
    if meta and meta["var_type"]:
      var_type = meta["var_type"]
    elif self._current_scope.name == a_consts.ROOT_SCOPE:
      var_type = a_consts.VAR_TYPE.GLOBAL
    else:
      var_type = a_consts.VAR_TYPE.LOCAL
    if not variable:
      self.add_variable(variable_name, position, var_type)
    else:
      self.update_variable(variable_name, variable.scope, position)

  def visit_FunctionDef(self, node, meta):
    scope = self.create_scope(node.name)
    args = node.args.args
    for arg in args:
      self.add_variable(arg.id, position_block.Position.get_position(arg), a_consts.VAR_TYPE.ARG)
    for child in node.body:
      self.visit(child, meta)
    self._current_scope = scope.parent

  def dump(self, store_name):
    json_dict = {}
    for scope, variables in self.scope_variable_map.items():
      json_dict[str(scope)] = variables
    cache.store_json(json_dict, store_name)

  def update_danglings(self):
    for scope in self.scopes.values():
      for var_name, positions in scope.get_danglings().items():
        par_scope = scope.parent
        while par_scope and par_scope in self.scope_variable_map:
          if var_name in self.scope_variable_map[par_scope]:
            self.scope_variable_map[par_scope][var_name].positions.update(positions)
            break
          par_scope = par_scope.parent
      scope.set_danglings({})

  def parse(self):
    source_code = cache.read_file(self.file_path)
    tree = ast.parse(source_code)
    self.visit(tree)
    self.update_danglings()
    return self

  def print_variables(self):
    for scope, variable_map in self.scope_variable_map.items():
      print("\n\n### Scope: %s\n" % str(scope))
      for variable in variable_map.values():
        print("Variable: %s, Type: %s" % (variable.name, variable.type and variable.type.name))
        print("Positions: ", variable.positions)
        print("Store Positions: ", variable.get_store_positions())
        print("Update Positions: ", variable.get_updated_positions())

