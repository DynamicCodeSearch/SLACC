import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import astor

from analysis.helpers import constants as a_consts
from analysis.blocks import statements as statement_block
from utils.lib import O

import properties


class Method(O):
  def __init__(self, **kwargs):
    self.file_source = None
    self.name = None
    self.return_type = None
    self.start_pos = None
    self.end_pos = None
    self.args = None
    self.statement_blocks = []  # [<Statements>]
    self._statement_groups = None  # [[<Statements>], [<Statements>]]
    self._ast = None
    self._scope = None
    self._prerequisite_statements = []
    O.__init__(self, **kwargs)

  def get_ast(self):
    return self._ast

  def get_scope(self):
    return self._scope

  def is_root(self):
    return self.name == a_consts.ROOT_SCOPE

  def split_statement_blocks(self):
    split = None
    for i, statement in enumerate(self.statement_blocks):
      if isinstance(statement, Method):
        split = i
    if split is None:
      return self.statement_blocks
    else:
      self._prerequisite_statements, statements = self.statement_blocks[:split+1], self.statement_blocks[split+1:]
    return statements

  def get_statement_groups(self):
    if self._statement_groups is not None:
      return self._statement_groups
    # self._statement_groups = Method.create_statement_groups(self.statement_blocks)
    # return self._statement_groups
    _statement_groups = []
    method_statement_blocks = self.split_statement_blocks()
    groups = Method.create_statement_groups(method_statement_blocks)
    for group in groups:
      combinations = Method.get_combinations(group)
      if combinations and len(combinations) > 0:
        _statement_groups += combinations
    for statement in method_statement_blocks:
      if isinstance(statement, statement_block.GroupedStatement) or \
         isinstance(statement, statement_block.ChoiceGroupedStatement):
        _statement_groups.append([statement])
    self._statement_groups = []
    if len(self._prerequisite_statements) >= properties.MIN_STATEMENT_SIZE:
      self._statement_groups.append(self._prerequisite_statements)
    for _statement_group in _statement_groups:
      _statement_group = self._prerequisite_statements + _statement_group
      if len(_statement_group) >= properties.MIN_STATEMENT_SIZE:
        self._statement_groups.append(_statement_group)
    return self._statement_groups

  def get_text(self):
    return astor.to_source(self._ast).strip("\n")

  def pprint(self):
    print(self.get_text())

  @staticmethod
  def print_statement_group(groups):
    for combination in groups:
      print("\n*** Combination ***")
      for statement in combination:
        statement.pprint()
      print("********************")

  @staticmethod
  def create_statement_groups(statement_blocks):
    if not statement_blocks: return []
    ret_list = []
    statement_group = []
    for statement in statement_blocks:
      statement_group.append(statement)
      if isinstance(statement, statement_block.GroupedStatement):
        sub_ret_list = Method.create_statement_groups(statement.statements)
        if sub_ret_list:
          ret_list += sub_ret_list
      elif isinstance(statement, statement_block.ChoiceGroupedStatement):
        for choice in statement.choices:
          sub_ret_list = Method.create_statement_groups(choice)
          if sub_ret_list:
            ret_list += sub_ret_list
    # min_size = properties.MIN_STATEMENT_SIZE
    min_size = 1
    if len(statement_group) >= min_size:
      ret_list.append(statement_group)
    return ret_list

  @staticmethod
  def get_combinations(statement_blocks):
    step_start = properties.MIN_STATEMENT_SIZE
    # step_start = 1
    combinations = []
    for step_size in xrange(step_start, len(statement_blocks)):
      for counter in xrange(0, len(statement_blocks) - step_size + 1):
        combinations.append(statement_blocks[counter: counter + step_size])
    combinations.append(statement_blocks)
    return combinations

