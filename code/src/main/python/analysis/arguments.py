import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from analysis.parsers import arg_parser
from analysis.tracer import Tracer


def parse_file_for_args(file_name):
  variable_visitor = arg_parser.VariableVisitor.parse(file_name)
  tracer = Tracer(variable_visitor)
  sys.settrace(tracer.trace_calls)
  exec("import %s" % file_name.split(".")[0])
  sys.settrace(None)
  print(variable_visitor.dump("temp.json"))
  return variable_visitor


parse_file_for_args("dummy.py")