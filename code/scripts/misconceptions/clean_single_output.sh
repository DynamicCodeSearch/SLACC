#!/usr/bin/env bash

#SBATCH --job-name clean_single_output
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

cd src/main/python
python misconceptions/cleaner/clean_single_output.py
