# Python script


The python scripts here are in different shapes of rewrite and could change form at any time.

## findthatpod.py
This is the old original script that was used to render the original findthatpod.opml from findthatpod.yaml. this was done by just parsing the data as it appeared in the YAML file and spit it out to the console with simple formatting.


## render-opml.py
This is the new(er) variation, yes it build upon the old script but utilized command line option, a filepath for the YAML. Then it just do what the old script did, spit it out at the console with some formatting.


## at the command line
To render the OPML from the YAML files, do something similar to what is below here;

```
python3 render-opml.py ../yaml/findthatpod-the-best-fiction-podcasts.yaml > ../findthatpod-the-best-fiction-podcasts.opml
python3 render-opml.py ../yaml/findthatpod-the-best-history-podcasts.yaml > ../findthatpod-the-best-history-podcasts.opml
python3 render-opml.py ../yaml/findthatpod-the-best-science-podcasts.yaml > ../findthatpod-the-best-science-podcasts.opml
python3 render-opml.py ../yaml/findthatpod-the-best-technology-podcasts.yaml > ../findthatpod-the-best-technology-podcasts.opml
python3 render-opml.py ../yaml/findthatpod-the-best-true-crime-podcasts.yaml > ../findthatpod-the-best-true-crime-podcasts.opml
```


The old script can be invoked manually or through the bash shell script, the shell script adds some automation.
