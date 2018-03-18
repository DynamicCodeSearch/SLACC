#!/bin/bash

#SBATCH --job-name codeseer_uniform
#SBATCH -N 8
#SBATCH -n 32
#SBATCH -p opteron
#SBATCH -x c[79-98, 101-107]
# Use modules to set the software environment

python fuzz/uniform.py 2
