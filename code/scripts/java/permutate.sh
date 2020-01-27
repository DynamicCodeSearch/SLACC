#!/usr/bin/env bash

#SBATCH --job-name permutate
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


if [ -z "$1" ]
then
    echo "Run: sh scripts/java/permutate.sh 'Dataset' args ... "
    exit 1
fi

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar permutate $1

echo "\n\nBuilding generated files"
cd ../projects
mvn clean install

cp ../projects/target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars/

echo "\n\nBuilding source code again"
cd ../code
mvn clean install