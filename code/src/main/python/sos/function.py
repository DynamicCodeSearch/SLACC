import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils.lib import O
from utils import cache, lib
import properties


def load_inputs(dataset, args_key):
  args_index = cache.load_json(lib.get_dataset_arg_index(dataset))
  if args_key not in args_index:
    return None
  arg_files_name = os.path.join(lib.get_dataset_args_folder(dataset), "%s.json" % args_index[args_key])
  arguments = cache.load_json(arg_files_name)
  assert len(arguments) == properties.FUZZ_ARGUMENT_SIZE
  return arguments


def is_array(arg_sets):
  if not type(arg_sets[0]) is list:
    return False
  return len(arg_sets[0]) != len(arg_sets[1]) != len(arg_sets[2])


class InputCache(O):
  _cache = {}

  @staticmethod
  def load(dataset, key):
    if key in InputCache._cache:
      return InputCache._cache[key]
    arguments = load_inputs(dataset, key)
    if arguments is None:
      return None
    if is_array(arguments):
      key_args = arguments
    else:
      key_args = [[] for _ in range(len(arguments[0]))]
      for i in range(len(arguments[0])):
        for arg in arguments:
          key_args[i].append(arg)
    InputCache._cache[key] = key_args
    return key_args


class Function(O):
  _id = 0

  def __init__(self, **kwargs):
    Function._id += 1
    self.id = Function._id
    self.name = None
    self.body = None
    self.dataset = None
    self.package = None
    self.className = None
    self.source = None
    self.lines_touched = None
    self.span = None
    self.input_key = None
    self.return_attribute = None
    self.outputs = None
    # Meta-info
    self.useful = None
    O.__init__(self, **kwargs)

  def clone(self):
    new = Function()
    for key in self.has().keys():
      if key == "id": continue
      new[key] = self[key]
    return new

  def is_useful(self):
    # TODO: check usefulness of function
    if self.useful is not None:
      return self.useful
    inputs = InputCache.load(self.dataset, self.input_key)
    if inputs is None:
      self.useful = False
      return self.useful
    only_none = True
    for retrn in self.outputs.returns:
      if retrn is not None:
        only_none = False
        break
    if only_none:
      self.useful = False
      return self.useful
    return_not_nones_indices = []
    for i in range(len(self.outputs.returns)):
      if self.outputs.returns[i] is not None:
        return_not_nones_indices.append(i)
    if len(return_not_nones_indices) == 0:
      self.useful = False
      return self.useful
    for input_arg in inputs:
      is_valid_input = False
      for i in return_not_nones_indices:
        if input_arg[i] != self.outputs.returns[i]:
          is_valid_input = True
          break
      if not is_valid_input:
        self.useful = False
        return self.useful
    self.useful = True
    return self.useful


class Outputs(O):
  def __init__(self, outputs_json=None, **kwargs):
    O.__init__(self, **kwargs)
    self.returns = []
    self.errors = []
    self.durations = []
    if outputs_json is not None:
      for output_json in outputs_json:
        self.returns.append(output_json["return"] if "return" in output_json else None)
        self.errors.append(output_json["errorMessage"] if "errorMessage" in output_json else None)
        self.durations.append(output_json["duration"] if "duration" in output_json else None)

  def clone(self):
    new = Outputs()
    new.returns = self.returns[:]
    new.errors = self.errors[:]
    new.durations = self.durations[:]
    return new
