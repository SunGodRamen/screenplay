#!/usr/bin/env sh

# Set the project root directory
PROJECT_ROOT="$(dirname "$(realpath "$0")")/.."

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

# Set the directories
FOUNTAIN_DIR="$PROJECT_ROOT/fountain"
PDF_DIR="$PROJECT_ROOT/pdf"

# Create the pdf directory if it doesn't exist
mkdir -p "$PDF_DIR"

# Proceed with the actual script
for s in "$FOUNTAIN_DIR"/*.fountain
do
    filename=$(basename "$s" .fountain)
    screenplain --format pdf "$s" "$PDF_DIR/$filename.pdf"
done

