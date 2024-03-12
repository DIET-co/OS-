#!/bin/sh
#echo "enter first number"
number1=5
#echo "enter second  number"
number2=5
#expr $number1 + $number2
 #back quotes used ofr assigning expresseion result to another varikable
#res=`expr $number1 \* $number2`   
res=`expr $number1 + $number2`   
echo "the result is: $res"

