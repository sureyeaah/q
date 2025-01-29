#!/usr/bin/env bash

for session in $(screen -ls | grep -o '[0-9]*\.\S*')
do
  screen -S "${session}" -X quit
done
