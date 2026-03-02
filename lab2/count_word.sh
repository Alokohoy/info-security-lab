#!/bin/bash
if [ $# -ne 2 ]; then
  echo "Usage: $0 <filename> <word>"
  exit 1
fi

filename="$1"
word="$2"

if [ ! -f "$filename" ]; then
  echo "Error: File '$filename' not found."
  exit 1
fi

count=$(grep -o -i -w "$word" "$filename" | wc -l | tr -d ' ')
echo "The word '$word' appears $count time(s) in '$filename'."
