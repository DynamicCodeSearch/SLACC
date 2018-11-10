from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

c=5.0

lst = []
dic = {}
tup = (1,2,3)

def func_a(x,y,z):
  def local(d):
    return d**2
  global c
  a = 5
  b = 10
  if a > 10:
    b += 1
  elif a > 20:
    b += 2
    c = c + 1
  elif a > 30:
    b += 3
    c = c + 2
  else:
    b += 4
    c = c + 3
  for i in range(4):
    a *= 2
    b += 1
    lst.append(a+b)
    dic[a] = a + b + sum(tup)

  return a+b+c * y**z * local(x)


# def func_b():
#   for i in range(4):
#     lst.append(i)

func_a(1,2,3)
# func_b()

