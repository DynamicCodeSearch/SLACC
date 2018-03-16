#!/bin/bash

#SBATCH --job-name codeseer_extract_functions
#SBATCH -N 8
#SBATCH -n 32
#SBATCH -p opteron
### Use modules to set the software environment

python utils/google_storage.py -n 32
