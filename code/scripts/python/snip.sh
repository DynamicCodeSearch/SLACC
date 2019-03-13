#!/usr/bin/env bash

#SBATCH --job-name snip
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/python/snip.sh 'Dataset' args ... "
    exit 1
fi

cd src/main/python
if [ -z "$2" ]
then
    find ~/Raise/ProgramRepair/CodeSeer/projects/src/main/python/$1  -name "generated_py_*.py" -type f -delete
    find ~/Raise/ProgramRepair/CodeSeer/projects/src/main/python/$1  -name "tmp_py_*.py" -type f -delete
    python mains/snipper.py $1
else
    find ~/Raise/ProgramRepair/CodeSeer/projects/src/main/python/$1/$2  -name "generated_py_*.py" -type f -delete
    find ~/Raise/ProgramRepair/CodeSeer/projects/src/main/python/$1/$2  -name "tmp_py_*.py" -type f -delete
    python mains/snipper.py $1 $2
fi


## Codejam
#sbatch scripts/python/snip.sh CodeJam
#--- OR ---
#sbatch scripts/python/snip.sh CodeJam Y11R5P1
#sbatch scripts/python/snip.sh CodeJam Y12R5P1
#sbatch scripts/python/snip.sh CodeJam Y13R5P1
#sbatch scripts/python/snip.sh CodeJam Y14R5P1
