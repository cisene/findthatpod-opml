#!/usr/bin/env bash

#
python3 findthatpod.py > ../findthatpod.opml

# Add yaml source to commit
git add ../yaml/findthatpod.yaml

# Add output to commit
git add ../findthatpod.opml

# Add issues to commit
git add ../findthatpod-issue-*.opml

# Commit and Push
git commit -m "Updates through automation"
git push
