#!/usr/bin/env bash

#SBATCH --job-name random_testing
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


if [ -z "$1" ]
then
    echo "Run: sh scripts/common/test/random_testing.sh 'Dataset' 'nfolds'... "
    exit 1
fi

cd src/main/python
if [ -z "$2" ]
then
    python sos/analyze.py random_testing $1
else
    python sos/analyze.py random_testing $1 $2
fi


## Codejam
#sh scripts/common/test/random_testing.sh CodeJam
#--- OR ---
#sh scripts/common/test/random_testing.sh CodeJam 10