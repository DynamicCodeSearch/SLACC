#!/usr/bin/env bash

#SBATCH --job-name cluster_testing
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


if [ -z "$1" ]
then
    echo "Run: sh scripts/common/test/cluster_testing.sh 'Dataset' 'Language' ... "
    exit 1
fi

cd src/main/python
if [ -z "$2" ]
then
    python sos/analyze.py cluster_testing $1
else
    python sos/analyze.py cluster_testing $1 $2
fi


## Codejam
#sh scripts/common/test/cluster_testing.sh CodeJam
#--- OR ---
#sh scripts/common/test/cluster_testing.sh CodeJam java_python
