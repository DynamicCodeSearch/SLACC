#!/bin/bash

#SBATCH --job-name codeseer
#SBATCH -N 16
#SBATCH -p opteron
# Use modules to set the software environment

python utils/google_storage.py -n 48 -o main
