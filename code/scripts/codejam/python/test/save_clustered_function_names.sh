#!/usr/bin/env bash

#SBATCH --job-name cluster
#SBATCH -N 1
#SBATCH -p opteron

## Use modules to set the software environment

cd src/main/python
python sos/analyze.py save_function_names codejam java_python