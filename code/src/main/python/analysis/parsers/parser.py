from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import ast

NODE_CONST_KEYS = {'first_token', 'last_token', 'lineno', 'col_offset'}


class Traveller(object):
  """
  A node visitor base class that walks the abstract syntax tree and calls a
  visitor function for every node found.  This function may return a value
  which is forwarded by the `visit` method.

  This class is meant to be subclassed, with the subclass adding visitor
  methods.

  Per default the visitor functions for the nodes are ``'visit_'`` +
  class name of the node.  So a `TryFinally` node visit function would
  be `visit_TryFinally`.  This behavior can be changed by overriding
  the `visit` method.  If no visitor function exists for a node
  (return value `None`) the `generic_visit` visitor is used instead.
  """

  def __init__(self, defaults=None, caller=None):
    self.defaults = set(defaults) if defaults else set()
    self.caller = caller

  def visit(self, node, meta=None):
    """Visit a node."""
    node_name = node.__class__.__name__
    if self.caller and node_name in self.defaults:
      return self.caller(node, meta)
    method = 'visit_' + node.__class__.__name__
    default_method = self.generic_exit if meta and meta.get("stop_recursion", False) else self.generic_visit
    visitor = getattr(self, method, default_method)
    return visitor(node, meta)

  def generic_visit(self, node, meta=None):
    """Called if no explicit visitor function exists for a node."""
    for field, value in ast.iter_fields(node):
      if isinstance(value, list):
        for item in value:
          if isinstance(item, ast.AST):
            self.visit(item, meta)
      elif isinstance(value, ast.AST):
        self.visit(value, meta)

  def generic_exit(self, node, meta=None):
    pass


def parse_print(node, annotate_fields=True, include_attributes=True):
  print(ast.dump(node, annotate_fields, include_attributes))


def get_child_nodes(node):
  children = {}
  for key in node.__dict__.keys():
    if key not in NODE_CONST_KEYS:
      children[key] = node.__dict__[key]
  return children