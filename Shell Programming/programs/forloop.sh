#!/bin/bash
# using continue command

for i in 1 2 3 4 5 6 7 8 9
do
if [ $i -eq 5 ]
then
#break
continue
fi
echo "I is equal to: $i"
done
