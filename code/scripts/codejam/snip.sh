#!/usr/bin/env bash

#SBATCH --job-name snip_functions
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ $1 -e1 0 ]
then
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/*/*/generated_class_*.java
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/*/*/temp_class_*.java
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam snip
else
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/$1/*/generated_class_*.java
    rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/$1/*/temp_class_*.java
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam snip $1
fi