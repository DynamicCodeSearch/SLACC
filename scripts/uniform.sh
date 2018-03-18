#!/bin/bash

#SBATCH --job-name csUniform
#SBATCH -N 16
#####SBATCH -n 16
#SBATCH -p opteron
#SBATCH -x c[79-98, 101-107]
# Use modules to set the software environment

python fuzz/uniform.py 16
