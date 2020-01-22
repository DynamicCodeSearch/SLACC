import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from itertools import chain


def fancy_interleave(l1, l2):
  zipped = chain.from_iterable(zip(l1, l2))
  return "".join([str(x) for x in zipped])

#
# def problem2(l1, l2):
#   result = ""
#   for (e1, e2) in zip(l1, l2):
#     result += str(e1)
#     result += str(e2)
#   return result


def valid_interleave(l1, l2):
  result = ""
  a1, a2 = len(l1), len(l2)
  for i in range(max(a1, a2)):
    if i < a1:
      result += str(l1[i])
    if i < a2:
      result += str(l2[i])
  return result


def _main():
  print(fancy_interleave([1,2,3], [4,5,6,7]))
  # print(problem2([1,2,3], [4,5,6,7]))
  print(valid_interleave([1,2,3], [4,5,6,7]))


if __name__ == "__main__":
  _main()
