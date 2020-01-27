#!/usr/bin/env bash

#SBATCH --job-name initialize
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/common/initialize.sh '<dataset>'"
    exit 1
fi

echo "Clearing old results"
rm -rf meta_results/$1
rm -rf meta_store/$1

echo "\n\nBuilding projects"
cd ../projects
mvn clean install

mkdir -p ../code/jars
cp ../projects/target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars/

echo "\n\nBuilding source code"
cd ../code
mvn clean install

echo "\n\nClearing database"
cd src/main/python
python store/init_db.py $1