#!/usr/bin/env bash

#SBATCH --job-name preprocess
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/java/preprocess.sh 'Dataset' args ... "
    exit 1
fi

rm -rf ../projects/src/main/java/$1/*/*/generated_*.java

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar preprocess $1


echo "\n Building projects ..."

cd ../projects
mvn clean install

echo "\n Copying built jar into code ... "
cp target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars


## Codejam
#sbatch scripts/java/preprocess.sh CodeJam

## IntroClassJava
#sbatch scripts/java/preprocess.sh IntroClassJava

