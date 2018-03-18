#!/bin/bash

#SBATCH --job-name csExtractFunctions
#SBATCH -N 1
#SBATCH -p opteron
#SBATCH -x c[79-98, 101-107]
### Use modules to set the software environment

python c_utils/c_parser.py -n 1
