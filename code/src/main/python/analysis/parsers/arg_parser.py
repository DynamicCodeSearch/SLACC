import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import ast

from analysis import constants as a_consts
from analysis.blocks import position as position_block
from analysis.blocks import scope as scope_block
from analysis.blocks import types as types_block
from analysis.blocks import variable as variable_block
from analysis.parsers import parser
from utils import cache


class VariableVisitor(parser.Traveller):
  def __init__(self):
    parser.Traveller.__init__(self)
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

  @staticmethod
  def _is_variable_store(node):
    return types_block.BasicType.get_name(node.ctx) == "Store"

  def create_scope(self, name):
    scope = scope_block.Scope(name, self._current_scope)
    self.scopes[str(scope)] = scope
    self.scope_variable_map[scope] = {}
    self._current_scope = scope
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
    variable = variable_block.Variable(name=name, scope=self._current_scope, var_type=var_type, positions=[position])
    variable_map[name] = variable
    self.scope_variable_map[self._current_scope] = variable_map

  def update_variable(self, name, scope, position):
    variable = self.scope_variable_map.get(scope, {}).get(name, None)
    if not variable:
      raise RuntimeError("Variable with name '%s' not found in scope '%s'" % (name, scope.name))
    variable.positions.append(position)

  def visit_Name(self, node, meta):
    variable_name = node.id
    variable = self.find_variable(variable_name, self._current_scope)
    is_variable_store = VariableVisitor._is_variable_store(node)
    if not variable and not is_variable_store:
      # Might be loading a global variable
      return
    position = position_block.Position.get_position(node)
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

  @staticmethod
  def parse(file_name):
    source_code = cache.read_file(file_name)
    tree = ast.parse(source_code)
    visitor = VariableVisitor()
    visitor.visit(tree)
    # print(visitor.scope_variable_map)
    return visitor
