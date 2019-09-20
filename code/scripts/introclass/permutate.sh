#!/usr/bin/env bash

#SBATCH --job-name permutate
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


rm ~/Raise/ProgramRepair/CodeSeer/projects/src/main/java/IntroClassJava/*/*/permutated_class_*.java
sh scripts/java/permutate.sh IntroClassJava