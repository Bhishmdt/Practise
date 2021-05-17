#!/bin/bash
# Find word count of a string in a folder
filepath=`pwd`
str=$1
grep -wirho $str ~/My_Django_stuff/inventory/ | wc -w | awk -v var=$str '{print var "," $1}' >>$filepath/temp/output.txt