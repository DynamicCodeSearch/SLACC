#!/usr/bin/env bash

#SBATCH --job-name extract_primitive_args
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/java/extract_primitive_arguments.sh 'Dataset' args ... "
    exit 1
fi

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar extract_primitive_args $1
