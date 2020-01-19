#!/usr/bin/env bash


if [ -z "$1" ]
then
    echo "Run: sh scripts/common/analyze.sh 'Dataset'"
    exit 1
fi

cd src/main/python
python sos/analyze.py cluster_testing $1 java_python
python sos/analyze.py save_target $1 java_python java
python sos/analyze.py save_target $1 java_python python
python sos/analyze.py save_mixed $1 java_python
