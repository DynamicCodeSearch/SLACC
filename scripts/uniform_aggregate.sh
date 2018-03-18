#!/bin/bash

#SBATCH --job-name csAggUniform
#SBATCH -N 1
#SBATCH -p opteron
#SBATCH -x c[79-98,101-107]
### Use modules to set the software environment

python fuzz/uniform.py -f aggregate