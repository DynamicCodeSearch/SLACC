# SLACC: Simion-based Language Agnostic Code Clones
This repository contains source code and scripts to obtain results for the paper ["SLACC: Simion-based Language Agnostic Code Clones"]().

The repository contains two major folders.
* `code/` which contains all the source code and scripts to generate semantic cross language code clones.
* `projects/` which contains the datasets which can be checked for semantic code clones. Each dataset has its dedicated folder for all the supported languages. For example, for the dataset used in the ICSE paper(`CodeJam`), the java code for the projects are in the folder `SLACC/projects/src/main/java/CodeJam`; while the python code for the projects are in the folder `SLACC/projects/src/main/<language>/<dataset>`

## Setting it up
The artifacts for SLACC can be installed by following the instructions in [INSTALL.md](INSTALL.md). SLACC can either be setup from the [scratch](INSTALL.md#setting-up-from-scratch) or reusing the preconfigured [virtualbox image](#preconfigured-image). We would recommend using the preconfigured image for prototyping or running the `Example` dataset used in the motivation section of the paper. For running the `CodeJam` dataset, it might be best to setup from the scratch or use the image on a machine with atleast 16GB of memory and 2 processors.

## Datasets
* `CodeJam` : Study on four problems from Google Code Jam (GCJ) repository and their valid submissions in Java and Python. We use the first problem from the fifth round of GCJ from 2011 to 2014. Overall in this study, we consider 247 projects; 170 from Java and 77 from Python. 
* `Example`: A sample program that contains 3 (2 in python, 1 in java) implementations of interleaving of arrays used in the `Motivation` section of the paper. 

