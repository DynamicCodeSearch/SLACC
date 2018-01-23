#!/bin/bash

#SBATCH --job-name codeseer
#SBATCH -N 8
#SBATCH -p broadwell
# Use modules to set the software environment

python runners/shrink_csv.py 8
