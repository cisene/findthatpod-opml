#!/usr/bin/env bash

# Render main OPML + separate issues
python3 findthatpod.py > ../findthatpod.opml


# Render The Best
#python3 render-opml.py ../yaml/findthatpod-the-best-fiction-podcasts.yaml > ../findthatpod-the-best-fiction-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-history-podcasts.yaml > ../findthatpod-the-best-history-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-science-podcasts.yaml > ../findthatpod-the-best-science-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-true-crime-podcasts.yaml > ../findthatpod-the-best-true-crime-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-technology-podcasts.yaml > ../findthatpod-the-best-technology-podcasts.opml

#python3 render-opml.py ../yaml/findthatpod-the-best-podcasts-about-space.yaml > ../findthatpod-the-best-podcasts-about-space.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-podcasts-about-the-paranormal.yaml > ../findthatpod-the-best-podcasts-about-the-paranormal.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-economics-podcasts.yaml > ../findthatpod-the-best-economics-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-podcasts-about-buddhism.yaml > ../findthatpod-the-best-podcasts-about-buddhism.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-video-game-podcasts.yaml > ../findthatpod-the-best-video-game-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-podcasts-about-scams.yaml > ../findthatpod-the-best-podcasts-about-scams.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-celebrity-podcasts.yaml > ../findthatpod-the-best-celebrity-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-food-podcasts.yaml > ../findthatpod-the-best-food-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-sci-fi-podcasts.yaml > ../findthatpod-the-best-sci-fi-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-mental-health-podcasts.yaml > ../findthatpod-the-best-mental-health-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-book-podcasts.yaml > ../findthatpod-the-best-book-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-wondery-podcasts.yaml > ../findthatpod-the-best-wondery-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-business-podcasts.yaml > ../findthatpod-the-best-business-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-motivational-podcasts.yaml > ../findthatpod-the-best-motivational-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-serial-killer-podcasts.yaml > ../findthatpod-the-best-serial-killer-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-poker-podcasts.yaml > ../findthatpod-the-best-poker-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-podcasts-for-dog-owners.yaml > ../findthatpod-the-best-podcasts-for-dog-owners.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-tech-podcasts.yaml > ../findthatpod-the-best-tech-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-dc-comics-podcasts.yaml > ../findthatpod-the-best-dc-comics-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-investigative-journalism-podcasts.yaml > ../findthatpod-the-best-investigative-journalism-podcasts.opml
#python3 render-opml.py ../yaml/findthatpod-the-best-comedy-podcasts.yaml > ../findthatpod-the-best-comedy-podcasts.opml


cd ../

# Delete empty files 
find ./ -type f -empty -delete


