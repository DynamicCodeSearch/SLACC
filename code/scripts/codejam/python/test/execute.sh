#!/usr/bin/env bash

#SBATCH --job-name reexecute_functions
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

cd src/main/python
python codejam/reexecutor.py
