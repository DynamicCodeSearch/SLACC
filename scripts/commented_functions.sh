#!/bin/bash

#SBATCH --job-name codeseer
#SBATCH -N 8
#SBATCH -p opteron
# Use modules to set the software environment

python runners/commented_functions.py 8
