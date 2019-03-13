#!/usr/bin/env bash

#SBATCH --job-name reexecute_functions
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/python/test/execute.sh 'Dataset' args ... "
    exit 1
fi

cd src/main/python
python mains/reexecutor.py $1
