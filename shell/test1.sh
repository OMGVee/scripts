#!/bin/sh
echo "creating an empty file named : dump.txt"
touch dump.txt
echo "filling it up with the local dir structure"
cat >> dump.txt
ls -alh >> dump.txt
