#!/usr/bin/env bash

#SBATCH --job-name crawl
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

rm -rf ../projects/src/main/IntroClassJava

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar IntroClass crawl

echo "\nFinished Downloading. Building projects ..."

cd ../projects
mvn clean install

echo "\nCopying built jar into code ... "
cp target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars

echo "\nFinished Downloading. Building code ..."
cd ../code
mvn -Dhttps.protocols=TLSv1.2 clean install
