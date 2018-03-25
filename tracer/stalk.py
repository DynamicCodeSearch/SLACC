"""
That function stalking module.
"""

from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import inspect
import ast
import asttokens
import logging
from utils.logger import get_logger
from utils.lib import O
import importlib
from utils import cache
from copy import deepcopy

LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)
BASE_PATH = 'data/pyfiles_dump/leetcode'
sys.path.insert(0, BASE_PATH)

VERBOSE = False


def pprint(*args):
  """
  Print if VERBOSE is true
  :param args: Values to be printed
  """
  if VERBOSE:
    print(*args)


def splice_list(l, s):
  """
  Splice a list "l" with "s" and return subtracted list
  :param l: Larger list
  :param s: Smaller list
  :return:
  """
  assert len(s) <= len(l)
  if len(s) == 0:
    return l
  elif s == l:
    return []
  for i in range(len(l)):
    if l[i] == s[0]:
      n = 1
      while n < len(s) and l[i + n] == s[n]:
        n += 1
      if n == len(s):
        return l[0: i] + l[i + n:]
  return None


def load_class(module_path, class_name="Solution"):
  """
  Load the class from module's path
  :param module_path: Path of the module
  :param class_name: Name of the class. Defaults to "Solution"
  :return:
  """
  module = importlib.import_module(module_path)
  return getattr(module, class_name)


def get_file(module_path):
  """
  Get the file name from module path
  :param module_path: Path of module. Separated by "."
  :return: Complete path of the file
  """
  return cache.create_file_path(BASE_PATH, "/".join(module_path.split(".")), ".py")


def parse_tree(file_name):
  """
  Parse the AST tree from the file and return all control blocks
  :param file_name: Name of the file
  :return: List of Blocks
  """
  blocks = []
  with open(file_name, 'rb') as py_file:
    tokenized_tree = asttokens.ASTTokens(py_file.read(), parse=True)
    for node in ast.walk(tokenized_tree.tree):
      if isinstance(node, Block.CODE_BLOCKS):
        block = Block(file_name)
        text = tokenized_tree.get_text(node)
        n_lines = len(text.split("\n"))
        block.start = node.lineno
        block.text = text
        block.end = node.lineno + n_lines - 1
        block.node = node
        blocks.append(block)
  return blocks


class Block(O):
  """
  Block of code
  """
  CODE_BLOCKS = (ast.For, ast.If, ast.While, ast.ListComp, ast.DictComp)

  def __init__(self, file_name):
    O.__init__(self)
    self.file_name = file_name
    self.start = None
    self.end = None
    self.text = None
    self.node = None


class Delta(O):
  """
  Delta between two StateChanges
  """
  def __init__(self, positives=None, negatives=None):
    O.__init__(self)
    self.positives = positives
    self.negatives = negatives

  @staticmethod
  def compute_delta(start_val, end_val):
    """
    Create instance of delta using the start val and end val of two objects
    :param start_val: Instance of int, float, set, str, dict, list
    :param end_val: Instance of int, float, set, str, dict, list
    :return:
    """
    assert type(start_val) == type(end_val)
    if type(end_val) in {int, float, set}:
      return Delta(positives=end_val - start_val, negatives=start_val - end_val)
    elif type(end_val) == str:
      return Delta(positives=end_val)
    elif type(end_val) == dict:
      keys = set(start_val.keys()).union(end_val.keys())
      positives, negatives = {}, {}
      for key in keys:
        if key in end_val:
          positives[key] = end_val[key]
        elif key in start_val:
          negatives[key] = start_val[key]
      return Delta(positives, negatives)
    elif type(end_val) == list:
      positives, negatives, spliced = None, None, None
      if len(end_val) > len(start_val):
        spliced = splice_list(end_val, start_val)
        positives = spliced
      elif len(start_val) > len(end_val):
        spliced = splice_list(start_val, end_val)
        negatives = spliced
      else:
        logger.info("Delta not implemented for different lists of equal length")
        return None
      if spliced is None:
        logger.info("Splicing did not work for %s and %s" % (start_val, end_val))
        return None
      return Delta(positives, negatives)
    else:
      logger.info("Delta computation not implemented for %s and %s of type %s" % (start_val, end_val, type(end_val)))
      return None

  def __eq__(self, other):
    if other is None:
      return False
    return self.positives == other.positives and self.negatives == other.negatives


class StateChange(O):
  """
  Start state of variable and end state of variable and delta between them
  """
  def __init__(self, start_state=None):
    O.__init__(self)
    self.start = start_state
    self.end = None
    self.deltas = {}

  def compute_deltas(self):
    """
    Compute delta between the start and end state
    :return:
    """
    if self.end is None:
      raise RuntimeError("Oops!! End state not present")
    start = self.start.locals
    end = self.end.locals
    # variables = set(start.keys()).union(end.keys())
    variables = start.keys()
    for variable in variables:
      if variable == "self": continue
      start_val = start.get(variable, None)
      end_val = end.get(variable, None)
      if start_val == end_val: continue
      if start_val is None:
        delta = Delta(positives=end_val)
      elif end_val is None:
        delta = Delta(negatives=end_val)
      else:
        delta = Delta.compute_delta(start_val, end_val)
      if delta is not None:
        self.deltas[variable] = delta


class TraceBlock(O):
  """
  An extended instance of Block with the state for a function input
  """
  def __init__(self, block, function_input):
    O.__init__(self)
    self.block = block
    self.function_input = function_input
    self.state_changes = []

  def is_in_scope(self, line_no):
    """
    Return in line number is in scope of function
    :param line_no:
    :return:
    """
    return self.block.start <= line_no <= self.block.end

  def get_state_changes(self):
    """
    Return changes of state in block
    :return:
    """
    deltas = []
    for state_change in self.state_changes:
      deltas.append(sorted(state_change.deltas.values()))
    return deltas

  def equals(self, other):
    """
    Check if trace-blocks are equal
    :param other:
    :return:
    """
    state_changes_1 = self.get_state_changes()
    state_changes_2 = other.get_state_changes()
    return self.function_input == other.function_input and state_changes_1 == state_changes_2


def clone(frame):
  """
  Clone an instance of trace frame
  :param frame: Instance of trace frame
  :return: Clone of a trace frame
  """
  return deepcopy(inspect.getargvalues(frame))


class Tracer(O):
  """
  Tracer class that contains tracer blocks and the name of the function to trace
  """
  def __init__(self, module_path, func_name, tracer_blocks):
    O.__init__(self)
    self.module = module_path
    self.func_name = func_name
    self.tracer_blocks = tracer_blocks
    self.stack = []
    self.current_block = None

  def get_block(self, line_no):
    """
    Get the block at the current line in the file
    :param line_no: Line number
    :return: Instance of tracer block.
    """
    for start_line, code_block in self.tracer_blocks.items():
      if line_no == start_line:
        return code_block
    return None

  def trace_calls(self, frame, event, _):
    """
    Trace function calls
    :param frame: Instance of the frame
    :param event: Name of the event
    :param _: Arg of the call
    :return: Trace line if it is a file
    """
    if event != 'call':
      return
    # print(frame.f_lineno)
    co = frame.f_code
    func_name = co.co_name
    # Ignore write() calls from print statements
    if func_name == 'write': return
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    pprint(func_line_no, func_filename)
    caller = frame.f_back
    if caller is None: return
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    pprint(caller_line_no, caller_filename)
    pprint('Call to %s on line %s of %s from line %s of %s' %
           (func_name, func_line_no, func_filename, caller_line_no, caller_filename))
    # Trace into this function
    if func_name == self.func_name:
      return self.trace_lines
    return

  def trace_lines(self, frame, event, _):
    """
    Trace each line in the function and mark changes of
    state at each frame.
    :param frame: Instance of the frame
    :param event: Name of the event
    :param _: Arg of the line
    :return:
    """
    if event != 'line':
      for block in self.stack:
        block.state_changes[-1].end = clone(frame)
        block.state_changes[-1].compute_deltas()
      # print(self.tracer_blocks)
      return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    pprint('  %s line %s' % (func_name, line_no))
    block = self.get_block(line_no)
    top = self.stack[-1] if len(self.stack) > 0 else None
    if top is None and block is None:
      return
    if top is not None and not top.is_in_scope(line_no):
      top.state_changes[-1].end = clone(frame)
      top.state_changes[-1].compute_deltas()
      self.stack.pop()
    if block is not None:
      if len(self.stack) == 0 or block != self.stack[-1]:
        block.state_changes.append(StateChange(clone(frame)))
        self.stack.append(block)
    pprint(len(self.stack))
    # print(inspect.getargvalues(frame))


def trace(module_path, func_name, *args):
  """
  Trace a function from the module and executing the args
  :param module_path: Path of the module
  :param func_name: Name of the function
  :param args: Args passed to the function
  :return:
  """
  tracer_blocks = {block.start: TraceBlock(block, args) for block in parse_tree(get_file(module_path))}
  tracer = Tracer(module_path, func_name, tracer_blocks)
  solution = load_class(module_path)
  sys.settrace(tracer.trace_calls)
  solution().twoSum(*args)
  return tracer


def cluster_blocks(blocks):
  for i in range(0, len(blocks) - 1):
    for j in range(i, len(blocks)):
      if i == j: continue
      if blocks[i].equals(blocks[j]):
        print("Wohoo")
        print((blocks[i].block.file_name, blocks[i].block.start))
        print((blocks[j].block.file_name, blocks[j].block.start))


def _verify_clustering():
  tracer1 = trace("1.1", "twoSum", [1, 2, 3, 4], 7)
  blocks1 = tracer1.tracer_blocks.values()
  tracer2 = trace("1.3", "twoSum", [1, 2, 3, 4], 7)
  blocks2 = tracer2.tracer_blocks.values()
  cluster_blocks(blocks1 + blocks2)


def _verify_deltas():
  tracer = trace("1.1", "twoSum", [1, 2, 3, 4], 7)
  blocks = tracer.tracer_blocks.values()
  for block in blocks:
    print(block.block.start, block.function_input)
    print(block.state_changes)
  print("\n*********\n")
  tracer = trace("1.3", "twoSum", [1, 2, 3, 4], 7)
  blocks = tracer.tracer_blocks.values()
  for block in blocks:
    print(block.block.start, block.function_input)
    print(block.state_changes)


if __name__ == "__main__":
  # print(trace("1.1", "twoSum", [1, 2, 3, 4], 11))
  _verify_clustering()
