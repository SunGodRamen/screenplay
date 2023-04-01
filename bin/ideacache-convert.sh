#!/usr/bin/env sh

# check for the required commands and libraries
if ! command -v y2s > /dev/null 2>&1; then
    echo "Error: y2s is not installed. Please install it and try again."
    exit 1
fi

if ! command -v screenplain > /dev/null 2>&1; then
    echo "Error: Screenplain is not installed. Please install it and try again."
    exit 1
fi

if ! python3 -c "import reportlab" > /dev/null 2>&1; then
    echo "Error: reportlab library is not installed. Please install it using 'pip install reportlab' and try again."
    exit 1
fi

# check for the required arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# set the input file path
input_file="$1"

# check that the input file exists
if [ ! -f "$input_file" ]; then
  echo "Error: Input file does not exist."
  exit 1
fi

# set the output file path
output_file=$2

# convert the YAML file to a plain text document using y2s
y2s "$input_file" > tmp.txt

# convert the plain text document to a PDF using Screenplain, if the output file doesn't exist or is older than the input file
if [ ! -e "$output_file" ] || [ "$input_file" -nt "$output_file" ]; then
    screenplain tmp.txt "$output_file"
fi

# delete the plain text document
rm tmp.txt
