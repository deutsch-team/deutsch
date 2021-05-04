#!/bin/bash

function deutsch() {
  FILE=$1
  DEU=".deutsch"
  if [[ $1 != *"$DEU"* ]] && [[ $1 != *".de"* ]]; then
    FILE+=DEU
  fi
  python /usr/share/deutsch/interpreter/main.py $FILE
}
