#!/usr/bin/env bash

# Render main OPML + separate issues
python3 findthatpod.py > ../findthatpod.opml

cd ../

# Delete empty files 
find ./ -type f -empty -delete


