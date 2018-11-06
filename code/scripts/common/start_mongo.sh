#!/usr/bin/env bash

#SBATCH --job-name start_mongo
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

sh $MONGO_HOME/mongod.sh start
