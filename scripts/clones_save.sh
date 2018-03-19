#!/bin/bash

#SBATCH --job-name csCloneSave
#SBATCH -N 1
#SBATCH -p opteron
#SBATCH -x c[79-98,101-107]
### Use modules to set the software environment

python ml/cluster.py -f save_clone