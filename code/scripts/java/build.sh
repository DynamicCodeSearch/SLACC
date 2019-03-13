#!/usr/bin/env bash

#SBATCH --job-name build
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


echo "\n Building projects ..."

cd ../projects
mvn clean install

echo "\n Copying built jar into code ... "
cp target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars

echo "\n Finished Downloading. Building code ..."
cd ../code
mvn -Dhttps.protocols=TLSv1.2 clean install