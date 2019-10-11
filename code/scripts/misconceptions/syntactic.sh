#!/usr/bin/env bash

#SBATCH --job-name syntactic
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

cd src/main/python
python misconceptions/common/syntactic.py $1 $2