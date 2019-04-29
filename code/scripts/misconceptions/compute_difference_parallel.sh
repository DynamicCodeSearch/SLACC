#!/usr/bin/env bash

sbatch scripts/misconceptions/compute_difference.sh 0 50
sbatch scripts/misconceptions/compute_difference.sh 50 100
sbatch scripts/misconceptions/compute_difference.sh 100 150
sbatch scripts/misconceptions/compute_difference.sh 150 200
sbatch scripts/misconceptions/compute_difference.sh 200 250
sbatch scripts/misconceptions/compute_difference.sh 250 300
sbatch scripts/misconceptions/compute_difference.sh 300 350
sbatch scripts/misconceptions/compute_difference.sh 350 400
sbatch scripts/misconceptions/compute_difference.sh 400 450
sbatch scripts/misconceptions/compute_difference.sh 450 500