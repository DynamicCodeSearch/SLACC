#!/bin/bash

#SBATCH --job-name csExtractFunctions
#SBATCH -N 4
#SBATCH -n 16
#SBATCH -p opteron
### Use modules to set the software environment

python c_utils/c_parser.py -n 16
