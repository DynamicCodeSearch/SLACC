#!/bin/bash

#SBATCH --job-name codeseer
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

python fuzz/uniform.py
