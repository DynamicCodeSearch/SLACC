import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import ast
import asttokens

from analysis import constants as a_consts
from analysis import arguments as arg_analysis
from analysis.blocks import method as method_block
from analysis.blocks import scope as scope_block
from analysis.blocks import position as position_block
from analysis.blocks import statements as statement_block
from analysis.parsers import parser
from utils import cache, logger


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_start_end(node):
  start = position_block.Position(*node.first_token.start)
  end = position_block.Position(*node.last_token.end)
  return start, end


class StatementVisitor(parser.Traveller):
  def __init__(self, file_path, variable_visitor=None):
    defaults = [  # Expressions
                "Call", "Expr", "UnaryOp", "UAdd", "USub", "Not", "Invert",
                "BinOp", "Add", "Sub", "Mult", "Div", "FloorDiv", "Mod", "Pow",
                "LShift", "RShift", "BitOr", "BitXor", "BitAnd", "BoolOp", "And", "Or",
                "Compare", "Eq", "NotEq", "Lt", "LtE", "Gt", "GtE", "Is", "In", "NotIn",
                "keyword", "IfExp", "Attribute",
                  # Subscripts
                "Subscript", "Index", "Slice", "ExtSlice",
                  # Comprehensions
                "ListComp", "SetComp", "GeneratorExp", "DictComp", "comprehension",
                  # Statements
                "Assign", "AugAssign", "Raise", "Delete",
                  # Function and Class Defs
                "Lambda", "Return", "Yield", "Global", "Nonlocal"
                  # Control Flow
                "Break", "Continue",
                ]
    parser.Traveller.__init__(self, defaults=defaults, caller=self.visit_statement)
    self.file_path = file_path
    if not variable_visitor:
      variable_visitor = arg_analysis.parse_file_for_args(file_path)
    self.statement_blocks = []
    self.statement_groups = []
    self.scope_variable_map = variable_visitor.scope_variable_map
    self.scopes = variable_visitor.scopes
    self._current_scope = scope_block.Scope(a_consts.ROOT_SCOPE, None)
    self.methods = []
    self.ast_tokenized = None

  def parse(self):
    source_code = cache.read_file(self.file_path)
    self.ast_tokenized = asttokens.ASTTokens(source_code, parse=True)
    self.visit(self.ast_tokenized.tree)
    for method in self.methods:
      print("Method Name: %s. Statement Blocks: %d" % (method.name, len(method.statement_blocks)))


  def create_scope(self, name):
    scope = scope_block.Scope(name, self._current_scope)
    self.scopes[str(scope)] = scope
    self.scope_variable_map[scope] = {}
    self._current_scope = scope
    return scope

  def is_valid_scope(self, scope):
    return str(scope) in self.scopes

  def get_method_arguments(self, scope):
    func_scope = self.scopes[str(scope)]
    variables = self.scope_variable_map[func_scope].values()
    args = {}
    for variable in variables:
      if variable.var_type == a_consts.VAR_TYPE.ARG:
        args[variable.name] = variable
    return args

  def visit_FunctionDef(self, node, meta):
    function_name = node.name
    self._current_scope = scope_block.Scope(function_name, self._current_scope)
    print(function_name)
    if not self.is_valid_scope(self._current_scope):
      LOGGER.warn("Function not found in scope: %s" % function_name)
      return
    start, end = get_start_end(node)
    args = self.get_method_arguments(self._current_scope)
    method = method_block.Method(file_source=self.file_path, name=function_name,
                                 start_pos=start, end_pos=end, args=args)
    if not meta:
      meta = {}
      prev_method = None
    else:
      prev_method = meta['method']
    prev_statements = meta.get('statements', None)
    meta['method'] = method
    meta['statements'] = method.statement_blocks
    for child in node.body:
      self.visit(child, meta)
    self._current_scope = self._current_scope.parent
    meta['method'] = prev_method
    meta['statements'] = prev_statements
    self.methods.append(method)
    # for statement in method.statement_blocks:
    #   print(statement)
    return method

  def visit_statement(self, node, meta):
    # print(self.ast_tokenized.get_text(node))
    statements = meta and meta.get('statements', None)
    method_name = self._current_scope.name
    start, end = get_start_end(node)
    statement = statement_block.Statement(file_source=self.file_path, method_name=method_name,
                                          start_pos=start, end_pos=end, ast=node)
    if statements is not None:
      statements.append(statement)
    else:
      self.statement_blocks.append(statement)
    return statement

  def visit_grouped_statement(self, node, meta):
    statements = meta and meta.get('statements', None)
    method_name = self._current_scope.name
    start, end = get_start_end(node)
    statement = statement_block.GroupedStatement(file_source=self.file_path, method_name=method_name,
                                                 start_pos=start, end_pos=end, ast=node)
    if statements is not None:
      statements.append(statement)
    else:
      self.statement_blocks.append(statement)
    return statement

  def wrapped_grouped_statement(self, node, meta):
    statement = self.visit_grouped_statement(node, meta)
    prev_statements = meta.get('statements', None)
    meta['statements'] = statement.statements
    for child in node.body:
      self.visit(child, meta)
    meta['statements'] = prev_statements
    # for stat in statement.statements:
    #   print(self.ast_tokenized.get_text(stat.ast))
    # exit(0)

  def visit_choice_grouped_statement(self, node, meta):
    statements = meta and meta.get('statements', None)
    method_name = self._current_scope.name
    start, end = get_start_end(node)
    statement = statement_block.ChoiceGroupedStatement(file_source=self.file_path, method_name=method_name,
                                                       start_pos=start, end_pos=end, ast=node)
    if statements is not None:
      statements.append(statement)
    else:
      self.statement_blocks.append(statement)
    return statement

  def visit_If(self, node, meta):
    statement = self.visit_choice_grouped_statement(node, meta)
    prev_statements = meta.get('statements', None)
    choice_node = node
    while choice_node:
      # print("XXXXXX\n")
      # parser.parse_print(choice_node, False, False)
      choice = []
      meta['statements'] = choice
      for child in choice_node.body:
        self.visit(child, meta)
      statement.choices.append(choice)
      if len(choice_node.orelse) == 1 and  isinstance(choice_node.orelse[0], ast.If):
        choice_node = choice_node.orelse[0]
      else:
        choice = []
        meta['statements'] = choice
        for child in choice_node.orelse:
          self.visit(child, meta)
        statement.choices.append(choice)
        break
    meta['statements'] = prev_statements
    # for choice in statement.choices:
    #   print("**** Choice ****")
    #   for stat in choice:
    #     print(self.ast_tokenized.get_text(stat.ast))
    #   print("")
    # exit(0)

  def visit_For(self, node, meta):
    self.wrapped_grouped_statement(node, meta)

  def visit_While(self, node, meta):
    self.wrapped_grouped_statement(node, meta)

  def visit_Try(self, node, meta):
    self.wrapped_grouped_statement(node, meta)

  def visit_TryFinally(self, node, meta):
    self.wrapped_grouped_statement(node, meta)

  def visit_TryExcept(self, node, meta):
    self.wrapped_grouped_statement(node, meta)

  def visit_With(self, node, meta):
    self.wrapped_grouped_statement(node, meta)




  # def get_last_statement(self, meta):
  #   if meta and 'statements' in meta:
  #     return meta['statements'][-1]
  #   return self.statement_blocks[-1]


def _test():
  visitor = StatementVisitor("dummy.py")
  print(visitor)
  visitor.parse()


if __name__ == "__main__":
  _test()