#!/usr/bin/env bash

sbatch scripts/misconceptions/compute_difference.sh 0 150
sbatch scripts/misconceptions/compute_difference.sh 150 300
sbatch scripts/misconceptions/compute_difference.sh 300 450
sbatch scripts/misconceptions/compute_difference.sh 450 600
sbatch scripts/misconceptions/compute_difference.sh 600 750
sbatch scripts/misconceptions/compute_difference.sh 750 900
sbatch scripts/misconceptions/compute_difference.sh 900 1050
sbatch scripts/misconceptions/compute_difference.sh 1050 1200
sbatch scripts/misconceptions/compute_difference.sh 1200 1350
sbatch scripts/misconceptions/compute_difference.sh 1350 1500
sbatch scripts/misconceptions/compute_difference.sh 1500 1700