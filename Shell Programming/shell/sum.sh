#!/bin/sh
echo "enter first number"
read number1
echo "enter second  number"
read number2
#expr $number1 + $number2
 #back quotes used ofr assigning expresseion result to another varikable
sum=`expr $number1 + $number2`   
echo "the sum is: $sum"

