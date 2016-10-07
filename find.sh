#!/bin/bash

echoerr() { echo "$@" 1>&2; }

for file in ./*.csv
do
	python3 try.py ${file}
	echoerr ${file}
done