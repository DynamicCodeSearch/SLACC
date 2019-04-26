#!/usr/bin/env bash

sbatch scripts/misconceptions/compute_difference.sh 0 100
sbatch scripts/misconceptions/compute_difference.sh 100 200
sbatch scripts/misconceptions/compute_difference.sh 200 300
sbatch scripts/misconceptions/compute_difference.sh 300 400
sbatch scripts/misconceptions/compute_difference.sh 400 500