#!/usr/bin/env bash

#SBATCH --job-name cluster
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/common/cluster.sh 'Dataset' '?Language' ... "
    exit 1
fi

cd src/main/python
if [ -z "$2" ]
then
    python sos/similarity.py $1
else
    python sos/similarity.py $1 $2
fi

## Codejam
#sbatch scripts/common/cluster.sh CodeJam java
#--- OR ---
#sbatch scripts/common/cluster.sh CodeJam python
#--- OR ---
#sbatch scripts/common/cluster.sh CodeJam java_python
