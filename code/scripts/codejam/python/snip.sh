#!/usr/bin/env bash

#SBATCH --job-name snip_functions
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Invalid command. Run: sbatch scripts/codejam/python/snip.sh <problem_id>"
else
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/python/$1/*/generated_py_*.py
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/python/$1/*/tmp_py_*.py
    cd src/main/python
    python codejam/snipper.py $1
fi
