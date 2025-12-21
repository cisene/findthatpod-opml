#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
from datetime import datetime

import yaml
from lxml import etree

SOURCE_YAML = '../yaml/findthatpod.yaml'

OUTPUT_FILENAME = '../findthatpod.opml'

BASE_URL_FTP = 'https://b19.se/data/opml/findthatpod/'

global config


def writeOPML(filepath, contents):
  s = "\n".join(contents) + "\n"
  with open(filepath, "w") as f:
    f.write(contents)

def LoadYamlConfig(filepath):
  global config
  with open(filepath, 'r') as stream:
    try:
      config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)
    finally:
      pass

  return config



def main():
  global config
  config = None

  filenames = []

  LoadYamlConfig(SOURCE_YAML)

  for issue in config['issues']:
    if "opml" in issue:
      if str(issue['opml']) not in filenames:
        filenames.append(str(issue['opml']))
      else:
        print(f"We found duplicate when attempted to add '{str(issue['opml'])}' to list")
        exit(1)

  issues_length = len(config['issues'])
  filenames_length = len(filenames)

  print(f"issues: {issues_length}, files: {filenames_length}")

  issue_count = 0

  for issue in config['issues']:
    if "podcasts" in issue:

      if "htmlUrl" not in issue:
        print(isseu['name'])
        #continue

      issue_title = issue['name']
      issue_opml = issue['opml']
      issue_pubDate = issue['date']
      issue_htmlUrl = issue['htmlUrl']

      opml_fullpath = f"../opml/{issue_opml}"

      # Skip is file exists already
      #if os.path.isfile(opml_fullpath):
      #  continue



      # Open OPML
      opml = etree.Element("opml", version = "2.0")

      # Open Head
      head = etree.SubElement(opml, "head")

      # Handle Title
      title_text = f"{config['global']['ownerName']} - {issue_title} ({issue_pubDate})"
      title = etree.Element("title")
      title.text = str(title_text)
      head.append(title)

      # Handle URL
      url_text = f"{issue_htmlUrl}"
      url = etree.Element("url")
      url.text = str(url_text)
      head.append(url)

      # Handle dateCreated
      datecreated_text = datetime.strptime(str(issue_pubDate), '%Y-%m-%d').strftime('%c +0000')
      dateCreated = etree.Element("dateCreated")
      dateCreated.text = str(datecreated_text)
      head.append(dateCreated)

      # Handle ownerName
      ownerName_text = f"{config['global']['ownerName']}"
      ownerName = etree.Element("ownerName")
      ownerName.text = str(ownerName_text)
      head.append(ownerName)

      # Handle ownerEmail
      ownerEmail_text = f"{config['global']['ownerEmail']}"
      ownerEmail = etree.Element("ownerEmail")
      ownerEmail.text = str(ownerEmail_text)
      head.append(ownerEmail)

      opml.append(head)

      comment_text = f" Source: {BASE_URL_FTP}{issue_opml} "
      comment = etree.Comment(comment_text)
      opml.append(comment)

      # Close head

      # Open body
      body = etree.Element("body")

      for podcast in issue['podcasts']:
        podcast_title = podcast['title']
        podcast_htmlUrl = podcast['htmlUrl']
        podcast_xmlUrl = podcast['xmlUrl']

        Outline = etree.Element("outline")
        Outline.set("type", "link")
        Outline.set("version", "RSS")
        Outline.set("language", "en")

        Outline.set("title", str(podcast_title))
        Outline.set("text", str(podcast_title))

        Outline.set("htmlUrl", str(podcast_htmlUrl))
        Outline.set("xmlUrl", str(podcast_xmlUrl))

        body.append(Outline)

      # Close body
      opml.append(body)

      opml_contents = etree.tostring(opml, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode()
      writeOPML(f"../opml/{issue_opml}", opml_contents)

      print(f"Wrote {issue_opml} ..")
      issue_count += 1

      #if issue_count >= 1:
      #  break

if __name__ == '__main__':
  main()
