#!/usr/bin/env bash

#SBATCH --job-name stop_mongo
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ $# -eq 0 ]
    then
        echo "Provide Job ID. eg. sh scripts/common/sh_stop_mongo.sh <job_id>"
        exit 1
fi

scancel $1
sh $MONGO_HOME/mongod.sh clear
