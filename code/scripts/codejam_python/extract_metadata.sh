#!/usr/bin/env bash

#SBATCH --job-name ex_func_meta
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

cd src/main/python
if [ -z "$1" ]
then
    python codejam/executor.py
else
    python codejam/executor.py $1
fi
