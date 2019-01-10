#!/usr/bin/env bash

#SBATCH --job-name preprocess
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

rm -rf ../projects/src/main/java/CodeJam/*/*/generated_*.java

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam preprocess


echo "\n Building projects ..."

cd ../projects
mvn clean install

echo "\n Copying built jar into code ... "
cp target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars
