#!/usr/bin/env sh

# Check for the screenplain command
if ! command -v screenplain > /dev/null 2>&1; then
    echo "Error: screenplain is not installed. Please install it and try again."
    exit 1
fi

# Check for the Python interpreter
if ! command -v python3 > /dev/null 2>&1; then
    echo "Error: Python3 is not installed. Please install it and try again."
    exit 1
fi

# Check for the reportlab library in Python
if ! python3 -c "import reportlab" > /dev/null 2>&1; then
    echo "Error: reportlab library is not installed. Please install it using 'pip install reportlab' and try again."
    exit 1
fi

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <fountain_file> <pdf_file>"
    exit 1
fi

FOUNTAIN_FILE="$1"
PDF_FILE="$2"

if [ ! -e "$PDF_FILE" ] || [ "$FOUNTAIN_FILE" -nt "$PDF_FILE" ]; then
    screenplain --format pdf "$FOUNTAIN_FILE" "$PDF_FILE"
    exit 1
else
    exit 0
fi

