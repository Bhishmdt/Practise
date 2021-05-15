#!/bin/bash
# Find all occurrences of a string in a folder
filepath=`pwd`
str=$1
grep -wir $str ~/My_Django_stuff/inventory/ | awk -F ":" -v var=$str '{print var "," $2}' >>$filepath/temp/output.txt
