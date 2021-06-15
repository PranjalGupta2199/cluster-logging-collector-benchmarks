#!/bin/bash
declare -i total=0

a=0
b=0

for i in {1..11}
do
    temp=$(wc -l /var/log/containers/fluentd.stresslog* | tail -1 | rev | cut -d" " -f2 | rev)
    if (( $i == 1 ))
    then 
        a=$temp
    fi

    if (( $i == 11 ))
    then 
        b=$temp
    fi

    echo "$i $temp"
    total=$(( $total + $temp ))
    sleep 10s
done;

echo $(( $b - $a ))
# echo $(echo ($total/$count | $bc)