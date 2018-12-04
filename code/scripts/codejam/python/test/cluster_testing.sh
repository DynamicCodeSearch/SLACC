#!/usr/bin/env bash

#SBATCH --job-name cluster_testing
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

cd src/main/python
python sos/analyze.py cluster_testing codejam java_python
