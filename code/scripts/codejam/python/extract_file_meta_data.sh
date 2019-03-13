#!/usr/bin/env bash

#SBATCH --job-name meta_extract
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


cd src/main/python

python codejam/file_meta_data.py $1