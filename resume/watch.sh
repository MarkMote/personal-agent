#!/bin/bash
# Simple watch script - recompiles on file change
# Usage: ./watch.sh
# Then open resume.pdf in a viewer that auto-refreshes (evince, okular, or browser)

FILE="resume.tex"
LAST_HASH=""

echo "Watching $FILE for changes... (Ctrl+C to stop)"
echo "Open resume.pdf in a PDF viewer"

while true; do
    CURRENT_HASH=$(md5sum "$FILE" | cut -d' ' -f1)
    if [ "$CURRENT_HASH" != "$LAST_HASH" ]; then
        echo "$(date +%H:%M:%S) - Recompiling..."
        pdflatex -interaction=nonstopmode "$FILE" > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "$(date +%H:%M:%S) - Done"
        else
            echo "$(date +%H:%M:%S) - Error (check resume.log)"
        fi
        LAST_HASH="$CURRENT_HASH"
    fi
    sleep 0.5
done
