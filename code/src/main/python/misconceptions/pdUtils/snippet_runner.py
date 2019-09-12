import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import pandas as pd
import numpy

INPUT_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/misconceptions/resources/titanic.csv"
OUTPUT_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/results/py_executed.csv"


def to_csv(obj):
  if type(obj).__module__ == "numpy":
    pd.DataFrame(obj).to_csv(OUTPUT_PATH)
  else:
    obj.to_csv(OUTPUT_PATH)

def evaluate(snippet):
  df = pd.read_csv(INPUT_PATH)[:10]
  res = eval(snippet)
  to_csv(res)


# evaluate("df.describe()")
# evaluate("df.Survived.values")
# evaluate("df.tail()")
# evaluate("df['Cabin'].apply(lambda x: str(x)[0])")
# evaluate("df.groupby('Ticket')['Name'].transform('count')")
# evaluate("numpy.mean(df, axis=0)")
# evaluate("df.Age.describe()")
# evaluate("df.as_matrix(columns=['Survived'])")
evaluate("df['Sex'].value_counts(normalize=True)")