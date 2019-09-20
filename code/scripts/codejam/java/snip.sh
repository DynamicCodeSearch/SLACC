#!/usr/bin/env bash

#SBATCH --job-name snip_functions
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/*/*/generated_class_*.java
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/*/*/temp_class_*.java
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar snip CodeJam
else
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/$1/*/generated_class_*.java
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/$1/*/temp_class_*.java
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar snip CodeJam $1
fi