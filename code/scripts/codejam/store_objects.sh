#!/usr/bin/env bash

#SBATCH --job-name store_objects
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam store_objects
