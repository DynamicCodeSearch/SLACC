#!/usr/bin/env bash

#SBATCH --job-name dce
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/java/extract_primitive_arguments.sh 'Dataset' args ... "
    exit 1
fi

echo "\n Building projects ..."

cd ../projects
mvn clean install

echo "\n Copying built jar into code ... "
cp target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars

echo "\n Finished Downloading. Building code ..."
cd ../code
mvn -Dhttps.protocols=TLSv1.2 clean install


echo "\n Removing dead code"
java -jar jars/proguard.jar @resources/dead_code_remove.pro


echo "\n Extracting jar"
java -jar jars/cfr.jar cleaned/projects-1.0-SNAPSHOT-jar-with-dependencies.jar --outputdir extracted

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar dead_code $1

echo "Deleting extracted"
rm -rf cleaned
rm -rf extracted