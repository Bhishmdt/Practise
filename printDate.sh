#!/bin/bash
# Print date every two min

while [ 1 ]
do
  date +%x >>/home/bhishm/Practise/Practise/temp/time.txt
  sleep 120
done