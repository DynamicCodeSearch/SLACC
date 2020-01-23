# SLACC: Simion-based Language Agnostic Code Clones
This repository contains source code and scripts to obtain results for the paper ["SLACC: Simion-based Language Agnostic Code Clones"]().

The repository contains two major folders.
* `code/` which contains all the source code and scripts to generate semantic cross language code clones.
* `projects/` which contains the datasets which can be checked for semantic code clones. Each dataset has its dedicated folder for all the supported languages. For example, for the dataset used in the ICSE paper(`CodeJam`), the java code for the projects are in the folder `SLACC/projects/src/main/java/CodeJam`; while the python code for the projects are in the folder `SLACC/projects/src/main/<language>/<dataset>`

## Setting it up
The artifacts for SLACC can be installed by following the instructions in [INSTALL.md](INSTALL.md). SLACC can either be setup from the [scratch](https://github.com/DynamicCodeSearch/SLACC/edit/ICSE20/INSTALL.md#setting-up-from-scratch) or reusing the preconfigured [virtualbox image](https://github.com/DynamicCodeSearch/SLACC/edit/ICSE20/INSTALL.md#preconfigured-image). We would recommend using the preconfigured image for prototyping or running the `Example` dataset used in the motivation section of the paper. For running the `CodeJam` dataset, it might be best to setup from the scratch or use the image on a machine with atleast 16GB of memory and 2 processors.

## Datasets
* `CodeJam` : Study on four problems from Google Code Jam (GCJ) repository and their valid submissions in Java and Python. We use the first problem from the fifth round of GCJ from 2011 to 2014. Overall in this study, we consider 247 projects; 170 from Java and 77 from Python. 
* `Example`: A sample program that contains 3 (2 in python, 1 in java) implementations of interleaving of arrays used in the `Motivation` section of the paper. 

## Running SLACC

#### Obtaining Datasets
##### For `CodeJam`
* The repository already contains the java and python files in `projects/src/main/java/CodeJam` and `projects/src/main/python/Codejam` respectively.
* To download these projects again, run 
```
> cd code
# For java
> sh scripts/codejam/java/download.sh
# For python
> sh scripts/codejam/python/download.sh
```
##### For `Example`
* The repository already contains the java and python files in `projects/src/main/java/Example` and `projects/src/main/python/Example` respectively.

#### Initializing SLACC

#### Running all stages for a dataset

#### Running each stage separately

2. **Snip**
  * Java:
    * For snipping the functions, run `sh scripts/java/snip.sh <dataset>`
    * For generating permutations, run `sh scripts/java/permutate.sh <dataset>`
  * Python:  
    * For snipping and permutating the functions, Run run `sh scripts/python/snip.sh <dataset>`
3. **Arguments - Metadata**
  * Java:
    * Store Objects: Run `sh scripts/java/store_objects.sh <dataset>`
    * Extract Primitive Arguments: Run `sh scripts/java/extract_primitive_arguments.sh <dataset>`
    * Extract Fuzzed Arguments: Run `sh scripts/java/extract_fuzzed_arguments.sh <dataset> <do_delete_old>`
  * Python:
    * Extract Metadata: Run `sh scripts/python/extract_metadata.sh <dataset>`
  * Arguments are stored in `primitive_arguments` and `fuzzed_arguments` collection in MongoDB
4. **Execute**
  * Java:
    * Run `sh scripts/java/execute.sh <dataset>`. Executed functions stored in `functions_executed` collection in mongo.
  * Python:
    * Run `sh scripts/python/execute.sh <dataset>`. Executed functions stored in `py_functions_executed` collection in mongo.
5. **Cluster**
  * Run `sh scripts/common/analyze.sh <dataset>`
  * Results stored in 
    * Clusters as txt and reusable pkl files are stored in `meta_results/<dataset>/clusters/`
    * Clusters are also stored in the database for thresholds varying between `0.01` and `0.30` in collections approporiately named as `clusters_<threshold>`
