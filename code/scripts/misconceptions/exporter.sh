#!/usr/bin/env bash

#SBATCH --job-name mis_exporter
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

cd src/main/python
python misconceptions/common/exporter.py