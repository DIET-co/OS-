#!/bin/sh
if [ -f displayhello.sh ]
then
echo "We have found the file!"
cat displayhello.sh
else
echo "Keep looking!"
fi
