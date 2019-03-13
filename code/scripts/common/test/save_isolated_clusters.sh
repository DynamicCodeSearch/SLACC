#!/usr/bin/env bash

#SBATCH --job-name tgt_clusters
#SBATCH -N 1
#SBATCH -p opteron

## Use modules to set the software environment


if [ -z "$1" ]
then
    echo "Run: sh scripts/common/test/save_clustered_function_names.sh 'Dataset' 'Language' ... "
    exit 1
fi

cd src/main/python
python sos/analyze.py save_target $1 java_python java
python sos/analyze.py save_target $1 java_python python
python sos/analyze.py save_mixed $1 java_python
