#!/bin/bash
# Find total word count in a folder

echo "Total occurrences"
find ~/My_Django_stuff/inventory/. -type f -exec cat {} + | wc -w
echo "Total words"
find ~/My_Django_stuff/inventory/. -type f -exec cat {} + | tr ' ' '\n' | sort -u | wc -l