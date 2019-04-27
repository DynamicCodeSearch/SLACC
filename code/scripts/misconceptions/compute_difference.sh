#!/usr/bin/env bash

#SBATCH --job-name diff
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

cd src/main/python
python misconceptions/common/compare.py $1 $2