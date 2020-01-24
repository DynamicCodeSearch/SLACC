#!/usr/bin/env bash

#SBATCH --job-name initialize
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/common/initialize.sh '<dataset>'"
    exit 1
fi


echo "\n\n 1) SNIPPING DATASET: $1 \n"

echo "\n For Java"
sh scripts/java/snip.sh $1
sh scripts/java/permutate.sh $1

echo "\n For Python"
sh scripts/python/snip.sh $1


echo "\n\n 2) EXTRACTING ARGUMENTS AND METADATA FOR DATASET: $1 \n"

echo "\n Storing Objects"
sh scripts/java/store_objects.sh $1

echo "\n Extracting Primitive Arguments"
sh scripts/java/extract_primitive_arguments.sh $1

echo "\n Extracting Fuzzed Arguments"Ø
sh scripts/java/extract_fuzzed_arguments.sh $1 True

echo "\n Extracting metadata for python"
sh scripts/python/extract_metadata.sh $1


echo "\n\n 3) EXECUTING SNIPPED FUNCTIONS FOR DATASET: $1 \n"

echo "\n For Java"
sh scripts/java/execute.sh $1

echo "\n For Python"
sh scripts/python/execute.sh $1


echo "\n\n 4) CLUSTERING FUNCTIONS FOR DATASET: $1 \n"
sh scripts/common/analyze.sh $1
