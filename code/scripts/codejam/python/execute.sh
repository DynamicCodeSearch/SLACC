#!/usr/bin/env bash

#SBATCH --job-name execute_functions
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Invalid command. Run: sbatch scripts/codejam/python/snip.sh <problem_id>"
else
    cd src/main/python
    python codejam/executor.py $1
fi
