#! /bin/bash
​
while :
do
  val=$(curl http://localhost:$1/metrics/ 2>&1 | grep $2 | tail -1 | rev | cut -d" " -f1 | rev)
  echo -n "$val, "
  ((i++))
  sleep 1m
done    