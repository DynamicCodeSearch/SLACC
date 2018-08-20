#!/usr/bin/env bash

#SBATCH --job-name download
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar crawl 11 5 1
java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar crawl 12 5 1
java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar crawl 13 5 1
java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar crawl 14 5 1

echo "Finished Downloading. Building projects"

cd ../projects
mvn clean install