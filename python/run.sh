#!/usr/bin/env bash

#
python3 findthatpod.py > ../findthatpod.opml

# 
git add ../findthatpod.opml

# Commit and Push
git commit -m "Updates through automation"
git push
