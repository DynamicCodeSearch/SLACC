from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

from utils.lib import O
from analysis import constants as a_consts
from analysis.blocks import types

__author__ = "bigfatnoob"

DEBUG = False


class Tracer(O):
  def __init__(self, variable_visitor, **kwargs):
    self.variable_visitor = variable_visitor
    O.__init__(self, **kwargs)

  def is_valid(self, scope_name):
    return scope_name != a_consts.ROOT_SCOPE and self.variable_visitor.get_scope(scope_name) is not None

  @staticmethod
  def get_scope(frame):
    scopes = []
    while frame:
      scope_name = frame.f_code.co_name
      if scope_name == "<module>":
        scopes.insert(0, a_consts.ROOT_SCOPE)
        frame = None
      else:
        scopes.insert(0, scope_name)
        frame = frame.f_back
    return a_consts.SCOPE_SEPARATOR.join(scopes)

  def trace_calls(self, frame, event, arg):
    if event != 'call':
      return
    co = frame.f_code
    func_name = co.co_name
    scope_name = Tracer.get_scope(frame)
    if not self.is_valid(scope_name):
      return
    line_no = frame.f_lineno
    filename = co.co_filename
    if DEBUG:
      print('Call to %s on line %s of %s' % (func_name, line_no, filename))
    # print(Tracer.get_scope(frame))
    # exit(0)
    return self.trace_lines

  def trace_lines(self, frame, event, arg):
    if event != 'line':
      return
    code = frame.f_code
    func_name = code.co_name
    line_no = frame.f_lineno
    if DEBUG:
      print('  %s line %s' % (func_name, line_no))
    scope = self.variable_visitor.get_scope(Tracer.get_scope(frame))
    for variable_name, value in frame.f_locals.items():
      variable = self.variable_visitor.find_variable(variable_name, scope)
      if variable and not types.BasicType.is_none(value):
        variable.var_type = types.get_type(value)
    for variable_name, value in frame.f_globals.items():
      variable = self.variable_visitor.find_variable(variable_name, scope)
      if variable and not types.BasicType.is_none(value):
        variable.var_type = types.get_type(value)

