#!/usr/bin/env bash

#SBATCH --job-name test_execute_functions
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$3" ]
then
    echo "Run: `sh scripts/java/test/execute_single_function.sh 'Dataset' 'file_path' 'function_name' ... `"
    exit 1
fi

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar test_reexecute_single $1 $2 $3