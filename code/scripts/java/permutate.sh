#!/usr/bin/env bash

#SBATCH --job-name permutate
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


if [ -z "$1" ]
then
    echo "Run: sh scripts/java/permutate.sh 'Dataset' args ... "
    exit 1
fi

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar permutate $1