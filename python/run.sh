#!/usr/bin/env bash

# Main and issues
python3 findthatpod.py > ../findthatpod.opml


# Render The Best
#python3 render-opml.py ../yaml/findthatpod-the-best-fiction-podcasts.yaml > ../findthatpod-the-best-fiction-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-history-podcasts.yaml > ../findthatpod-the-best-history-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-science-podcasts.yaml > ../findthatpod-the-best-science-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-technology-podcasts.yaml > ../findthatpod-the-best-technology-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-true-crime-podcasts.yaml > ../findthatpod-the-best-true-crime-podcasts.opml


# Add yaml source to commit
git add ../yaml/findthatpod.yaml

# Add output to commit
git add ../findthatpod.opml

# Add issues to commit
#git add ../findthatpod-issue-*.opml

# Add The Best to commit
#git add ../findthatpod-the-best-*.opml

# Commit and Push
git commit -m "Updates through automation"
git push
