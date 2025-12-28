#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
from datetime import datetime

import yaml

YAML_FINDTHATPOD_WEEKLY = '../yaml/findthatpod.yaml'
YAML_FINDTHATPOD_THEBEST = '../yaml/findthatpod-the-best-collections.yaml'

MD_README = '../README.md'

B19_PREFIX = 'https://b19.se/data/opml/findthatpod/'

def readYAML(filepath):
  content = None
  with open(filepath, 'r') as stream:
    try:
      content = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)
    finally:
      pass

  return content

def writeMarkdown(filepath, contents):
  s = "\n".join(contents) + "\n"
  with open(filepath, "w") as f:
    f.write(contents)


def main():
  buffer = []

  buffer.append(f"# FindThatPod - OPML Podcast Collections")
  buffer.append("\n")

  buffer.append("These OPML files are representations of the [FindThatPod](https://findthatpod.com/) weekly newsletters with podcast recommendations and also The Best of series that are released periodically as thematic collections of podcasts.")
  buffer.append("\n")

  buffer.append("All the material of the newsletters are property of FindThatPod, I have just rendererd an [OPML](https://en.wikipedia.org/wiki/OPML) out of them and make no claims to their work.")
  buffer.append("\n")

  buffer.append("Go to the [FindThatPod](https://findthatpod.com/) for more information.")
  buffer.append("\n")

  buffer.append("I just created something that I would like to consume myself, lists without links are useless, an [OPML](https://en.wikipedia.org/wiki/OPML) can be fed into just about ANY podcast catcher and be used right away.")
  buffer.append("\n")

  buffer.append("All collections are browseable and downloadable at [b19.se/data/opml/findthatpod/](https://b19.se/data/opml/findthatpod/).")


  buffer.append("\n\n")
  buffer.append(f"## The Best of ...")
  buffer.append("\n\n")

  data = readYAML(YAML_FINDTHATPOD_THEBEST)
  if data != None:
    buffer.append(f"| The Best of ..                                                                      | Date       |")
    buffer.append(f"| ----------------------------------------------------------------------------------- | ---------- |")

    for issue in data['issues']:
      if "podcasts" not in issue:
        continue

      if len(issue['podcasts']) < 1:
        continue

      line = []
      #print(issue)
    
      filename = issue['opml']
      #print(filename)

      line.append(f"| ")
      line.append(f"[FindThatPod - {issue['name']}]({B19_PREFIX}{filename})")
      line.append(f" | ")
      line.append(f"{issue['date']}")
      line.append(f" |")

      #| FindThatPod - The Best Fishing Podcasts                                             | 2025-06-18 |
      #| [FindThatPod - The Best Art Podcasts](https://b19.se/data/opml/findthatpod/findthatpod-the-best-art-podcasts.opml) | 2024-09-11 |

      table_line = "".join(line)
      #print(table_line)
      buffer.append(table_line)


  buffer.append("\n\n\n")
  buffer.append(f"## Weekly issues")
  buffer.append("\n\n")

  data = readYAML(YAML_FINDTHATPOD_WEEKLY)
  if data != None:
    buffer.append(f"| Weekly issues                                                                         | Date       |")
    buffer.append(f"| ------------------------------------------------------------------------------------- | ---------- |")

    #for issue in data['body']:
    for issue in data['issues']:
      line = []
      #print(issue)

      # findthatpod-issue-291.opml
      #filename = f"findthatpod-issue-{issue['issue']:03}.opml"
      opml = issue['opml']
      #print(filename)

      line.append(f"| ")
      #line.append(f"[{issue['title']}]({B19_PREFIX}{opml})")
      line.append(f"[{issue['name']}]({B19_PREFIX}{opml})")
      line.append(f" | ")
      #line.append(f"{issue['pubDate']}")
      line.append(f"{issue['date']}")
      line.append(f" |")
      # | [Find That Pod #291](https://b19.se/data/opml/findthatpod/findthatpod-issue-291.opml) | 2024-12-06 |

      table_line = "".join(line)
      buffer.append(table_line)


  doc = "\n".join(buffer)
  writeMarkdown(MD_README, doc)


if __name__ == '__main__':
  main()
