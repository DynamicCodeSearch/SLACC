#!/usr/bin/env bash

sbatch scripts/misconceptions/compute_difference.sh 0 100
sbatch scripts/misconceptions/compute_difference.sh 100 200
sbatch scripts/misconceptions/compute_difference.sh 200 300
sbatch scripts/misconceptions/compute_difference.sh 300 400
sbatch scripts/misconceptions/compute_difference.sh 400 500
sbatch scripts/misconceptions/compute_difference.sh 500 600
sbatch scripts/misconceptions/compute_difference.sh 600 700
sbatch scripts/misconceptions/compute_difference.sh 700 800
sbatch scripts/misconceptions/compute_difference.sh 800 900
sbatch scripts/misconceptions/compute_difference.sh 900 1000
sbatch scripts/misconceptions/compute_difference.sh 1000 1100