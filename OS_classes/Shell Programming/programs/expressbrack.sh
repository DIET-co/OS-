num=3

# y=`expr 5 + \( $num \* 3 \)`

y=`expr 5 \* \( $num + 3 \)`

echo $y
