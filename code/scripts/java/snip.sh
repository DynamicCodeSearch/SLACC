#!/usr/bin/env bash

#SBATCH --job-name snip
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/java/snip.sh 'Dataset' args ... "
    exit 1
fi

if [ -z "$2" ]
then
    find ../projects/src/main/java/$1  -name "generated_class_*.java" -type f -delete
    find ../projects/src/main/java/$1  -name "permutated_class_*.java" -type f -delete
    find ../projects/src/main/java/$1  -name "temp_class_*.java" -type f -delete
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar snip $1
else
    find ../projects/src/main/java/$1/$2  -name "generated_class_*.java" -type f -delete
    find ../projects/src/main/java/$1  -name "permutated_class_*.java" -type f -delete
    find ../projects/src/main/java/$1/$2  -name "temp_class_*.java" -type f -delete
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar snip $1 $2
fi

echo "\n\nBuilding generated files"
cd ../projects
mvn clean install

cp ../projects/target/projects-1.0-SNAPSHOT-jar-with-dependencies.jar ../code/jars/

echo "\n\nBuilding source code again"
cd ../code
mvn clean install


## Codejam
#sbatch scripts/java/snip.sh CodeJam
#--- OR ---
#sbatch scripts/java/snip.sh CodeJam Y11R5P1
#sbatch scripts/java/snip.sh CodeJam Y12R5P1
#sbatch scripts/java/snip.sh CodeJam Y13R5P1
#sbatch scripts/java/snip.sh CodeJam Y14R5P1

## IntroClassJava
#sbatch scripts/java/snip.sh IntroClassJava
#--- OR ---
#sbatch scripts/java/snip.sh IntroClassJava checksum
#sbatch scripts/java/snip.sh IntroClassJava digits
#sbatch scripts/java/snip.sh IntroClassJava grade
#sbatch scripts/java/snip.sh IntroClassJava median
#sbatch scripts/java/snip.sh IntroClassJava smallest
#sbatch scripts/java/snip.sh IntroClassJava syllables
