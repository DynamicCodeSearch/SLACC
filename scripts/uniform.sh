#!/bin/bash

#SBATCH --job-name csUniform
#SBATCH -N 16
#####SBATCH -n 16
#SBATCH -p opteron
# Use modules to set the software environment

python fuzz/uniform.py 16
