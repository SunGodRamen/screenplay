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

# Proceed with the actual script
for s in ./*.fountain
do
    screenplain --format pdf "$s" "pdf/${s%.fountain}.pdf"
done

