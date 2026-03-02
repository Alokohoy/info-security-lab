#!/bin/bash
if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

dir="$1"

if [ ! -d "$dir" ]; then
  echo "Error: '$dir' is not a directory."
  exit 1
fi

deleted=0
while IFS= read -r -d '' file; do
  echo "Deleted: $file"
  rm -f "$file"
  deleted=$((deleted + 1))
done < <(find "$dir" -maxdepth 1 -type f -empty -print0 2>/dev/null)

if [ $deleted -eq 0 ]; then
  echo "No empty files found in '$dir'."
fi
