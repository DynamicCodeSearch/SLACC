#!/bin/bash

#SBATCH --job-name codeseer
#SBATCH -N 8
###SBATCH -p broadwell
# Use modules to set the software environment

python utils/google_storage.py -n 8 -o george
