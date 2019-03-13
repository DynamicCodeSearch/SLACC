#!/usr/bin/env bash

#SBATCH --job-name save_fn_names
#SBATCH -N 1
#SBATCH -p opteron

## Use modules to set the software environment

cd src/main/python
python sos/analyze.py save_function_names codejam java_python

if [ -z "$1" ]
then
    echo "Run: sh scripts/common/test/save_clustered_function_names.sh 'Dataset' 'Language' ... "
    exit 1
fi

cd src/main/python
if [ -z "$2" ]
then
    python sos/analyze.py save_function_names $1
else
    python sos/analyze.py save_function_names $1 $2
fi


## Codejam
#sh scripts/common/test/save_clustered_function_names.sh CodeJam
#--- OR ---
#sh scripts/common/test/save_clustered_function_names.sh CodeJam java_python