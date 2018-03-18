#!/bin/bash

for run in {1..24}
do
  sbatch scripts/uniform.sh
done