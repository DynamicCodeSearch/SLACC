#!/usr/bin/env bash

#SBATCH --job-name tgt_clusters
#SBATCH -N 1
#SBATCH -p opteron

## Use modules to set the software environment

cd src/main/python
python sos/analyze.py save_target codejam java_python java
python sos/analyze.py save_target codejam java_python python
python sos/analyze.py save_mixed codejam java_python