#!/bin/bash

#SBATCH --job-name csUniform
#SBATCH -N 24
#####SBATCH -o out/%j.out
#####SBATCH -n 16
#SBATCH -p opteron
#SBATCH -x c[79-98,101-107]
# Use modules to set the software environment

python fuzz/uniform.py -n 48 -f fuzz
