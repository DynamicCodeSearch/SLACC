#!/usr/bin/env bash

#SBATCH --job-name download
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


cd src/main/python

python codejam/crawl.py 11 5 1
python codejam/crawl.py 12 5 1
python codejam/crawl.py 13 5 1
python codejam/crawl.py 14 5 1