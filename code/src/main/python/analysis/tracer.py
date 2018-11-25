from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

from utils.lib import O
from analysis.helpers import constants as a_consts
from analysis.blocks import types

__author__ = "bigfatnoob"

DEBUG = False


class Tracer(O):
  def __init__(self, variable_visitor, file_to_trace, ignores=[], **kwargs):
    self.variable_visitor = variable_visitor
    self.file_to_trace = file_to_trace
    self.ignores = ignores
    self.prev_line_no_map = {}
    self.lines_seen = set()
    O.__init__(self, **kwargs)

  def is_valid(self, scope_name):
    return scope_name is not None and \
           scope_name != a_consts.ROOT_SCOPE and \
           self.variable_visitor.get_scope(scope_name) is not None

  def get_scope(self, frame):
    if frame.f_code.co_filename != self.file_to_trace:
      return None
    scope_name = frame.f_code.co_name
    return self.variable_visitor.method_scopes.get(scope_name, None)
    # scopes = []
    # while frame:
    #   scope_name = frame.f_code.co_name
    #   if scope_name == "<module>":
    #     scopes.insert(0, a_consts.ROOT_SCOPE)
    #     frame = None
    #   elif scope_name in self.ignores:
    #     frame = frame.f_back
    #   else:
    #     scopes.insert(0, scope_name)
    #     frame = frame.f_back
    # return a_consts.SCOPE_SEPARATOR.join(scopes)

  def trace_calls(self, frame, event, arg):
    scope_name = self.get_scope(frame)
    if event != 'call':
      return
    co = frame.f_code
    func_name = co.co_name
    # scope_name = self.get_scope(frame)
    if not self.is_valid(scope_name):
      return
    line_no = frame.f_lineno
    filename = co.co_filename
    if DEBUG:
      print('Call to %s on line %s of %s' % (func_name, line_no, filename))
      # print(Tracer.get_scope(frame))
      # exit(0)
    self.prev_line_no_map[scope_name] = line_no
    return self.trace_lines

  def update_variable(self, variable_name, value, scope, line_no):
    variable = self.variable_visitor.find_variable(variable_name, scope)
    if not variable: return
    if not types.is_valid_type(value):
      variable.type = None
      return
    if DEBUG:
      print(variable_name, line_no)
    if not variable.is_type_set() and not types.BasicType.is_none(value):
      variable.type = types.get_type(value)
    position = variable and variable.get_position_by_line(line_no)
    if position is None:
      return
    prev_value = variable.get_prev_value()
    variable.set_prev_value(value)
    if variable.type is not None and variable.has_visited(position):
      return
    if not is_same(prev_value, value):
      variable.update_updated_position(position)
      if prev_value is None:
        variable.update_store_position(position)

  def trace_lines(self, frame, event, arg):
    # TODO: Add tracking line numbers for nested feature
    line_no = frame.f_lineno
    if event != 'line' and line_no in self.lines_seen:
      return
    self.lines_seen.add(line_no)
    code = frame.f_code
    func_name = code.co_name
    if DEBUG:
      print('  %s line %s' % (func_name, line_no))
    scope_name = self.get_scope(frame)
    scope = self.variable_visitor.get_scope(scope_name)
    prev_line_no = self.prev_line_no_map[scope_name]
    self.prev_line_no_map[scope_name] = line_no
    for variable_name, value in frame.f_locals.items():
      self.update_variable(variable_name, value, scope, prev_line_no)
    for variable_name, value in frame.f_globals.items():
      self.update_variable(variable_name, value, scope, prev_line_no)


def is_same(a, b):
  if type(a) != type(b):
    return False
  try:
    if a == b:
      return True
    else:
      return False
  except Exception as e:
    return (a == b).all()
  # if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
  #   return (a == b).all()
  # else:
  #   return a == b
