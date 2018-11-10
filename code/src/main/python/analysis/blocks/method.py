import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils.lib import O


class Method(O):
  def __init__(self, **kwargs):
    self.file_source = None
    self.name = None
    self.return_type = None
    self.start_pos = None
    self.end_pos = None
    self.args = None
    self.statement_blocks = [] # [<Statements>]
    self.statement_groups = [] # [[<Statements>], [<Statements>]]
    O.__init__(self, **kwargs)


