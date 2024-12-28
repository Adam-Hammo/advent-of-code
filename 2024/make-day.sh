#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <day number>"
    exit 1
fi

DAY_NUMBER=$1

mkdir -p input
touch "input/${DAY_NUMBER}.in"
touch "input/${DAY_NUMBER}s.in"

cp template.py "${DAY_NUMBER}.py"

echo "Files for AOC day ${DAY_NUMBER} created successfully."