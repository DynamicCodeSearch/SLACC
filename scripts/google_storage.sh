#!/bin/bash

#SBATCH --job-name codeseer
#SBATCH -N 4
#SBATCH -p broadwell
# Use modules to set the software environment

python utils/google_storage.py
