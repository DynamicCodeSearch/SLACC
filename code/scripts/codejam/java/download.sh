#!/usr/bin/env bash

#SBATCH --job-name download
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

rm -rf ../projects/src/main/java/CodeJam/Y*

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam crawl 11 5 1
java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam crawl 12 5 1
java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam crawl 13 5 1
java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar CodeJam crawl 14 5 1

echo "\nFinished Downloading. Building projects ..."

cd ../projects
mvn -Dhttps.protocols=TLSv1.2 clean install

echo "\nCopying built jar into code ... "
cp target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars

echo "\nFinished Downloading. Building code ..."
cd ../code
mvn -Dhttps.protocols=TLSv1.2 clean install
