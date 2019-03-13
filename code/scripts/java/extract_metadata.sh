#!/usr/bin/env bash

#SBATCH --job-name extract_metadata
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
#    echo "Run: sh scripts/java/extract_metadata.sh 'Dataset' args ... "
    exit
fi
java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar extract_metadata $1


