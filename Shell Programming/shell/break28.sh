#!/bin/bash
#breaking a loop
num=1
 while [ $num -lt 10 ]
 do
echo "$num"
if [ $num -eq 5 ] 
then
break
fi

num=`expr $num + 1`
done
echo "Loop is complete"

