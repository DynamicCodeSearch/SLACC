import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("white")

def plot():
  java_functions = np.cumsum([1680,1572,439,321,168])
  py_functions = np.cumsum([963,1015,498,382,277])
  mixed_functions = np.cumsum([62,63,6,0,0])
  funcs = np.transpose([java_functions, py_functions, mixed_functions])
  x = ["1", "2", "3", "4", "5"]
  # plt.figure()
  fig, ax = plt.subplots(figsize=(8, 4))

  ax.plot(np.arange(5), java_functions, '*-', label="Java")
  ax.plot(np.arange(5), py_functions, '*-',label="Python")
  ax.plot(np.arange(5), mixed_functions, '*-',label="Java + Python")
  ax.set_yscale("log")
  plt.ylabel("# Clones (Log Scale)", fontweight="bold", fontsize=16)
  plt.xlabel("# Arguments", fontweight="bold", fontsize=16)
  plt.xticks(np.arange(5), x)
  ax.tick_params(axis='both', which='major', labelsize=14)
  # ax.tick_params(axis='both', which='minor', labelsize=12)
  legend = ax.legend(shadow=True, fontsize=16)
  plt.tight_layout()
  plt.savefig("png_clones_vs_args.png")


plot()

def plot_bar():
  y = [271,811,843,747,753,502,275,281,383,364,288,261,279,252,227,184,132,101,73,66,69,55,53,46,24,28,31,7,4,36]
  x = map(str, range(1,30)) + ["30+"]
  indices = np.arange(len(x))
  plt.figure(figsize=(8, 3))
  plt.bar(indices, y)
  plt.xticks(indices, x)
  plt.xlabel("Lines of Code", fontweight="bold", fontsize=16)
  plt.ylabel("# Clones", fontweight="bold", fontsize=16)
  plt.tick_params(axis='y', which='major', labelsize=12)
  plt.tight_layout()
  plt.savefig("png_clones_vs_loc.png", bbox_inches='tight')



# plot_bar()

print(sum([271,811,843,747,753,502,275,281,383,364,288,261,279,252,227,184,132,101,73,66,69,50,43,46,24,28,31,7,4,36]))