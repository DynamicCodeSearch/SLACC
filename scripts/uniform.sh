#!/bin/bash

#SBATCH --job-name codeseer_uniform
#SBATCH -N 8
#SBATCH -n 32
#SBATCH -p opteron
# Use modules to set the software environment

python fuzz/uniform.py 2
