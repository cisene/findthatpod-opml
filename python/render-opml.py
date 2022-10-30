#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
from datetime import datetime

import yaml

SOURCE_YAML = '../yaml/findthatpod.yaml'

OUTPUT_FILENAME = '../findthatpod.opml'

global config

def htmlEncode(data):
  data = re.sub(r"\x26", "&amp;", str(data), flags=re.IGNORECASE)
  data = re.sub(r"\x27", "&#39;", str(data), flags=re.IGNORECASE)
  data = re.sub(r"\x22", "&#34;", str(data), flags=re.IGNORECASE)
  return data


def formatDateStringUTCNow():
  result = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S")
  return result

def formatDateString(data):
  dt = datetime.fromisoformat(data)
  datestr = dt.strftime("%a, %d %b %Y %H:%M:%S")
  return datestr


def ProcessItems(config):
  utc_now = datetime.now().isoformat()

  if config == None:
    print("config is empty")
    exit(0)

  opml_filename = None
  opml_origin = None
  if "opml" in config:

    if "filename" in config['opml']:
      opml_filename = config['opml']['filename']

    if "origin" in config['opml']:
      opml_origin = config['opml']['origin']

  opml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
  if opml_origin != None:
    opml += f"<!-- Source: {opml_origin} -->\n"
  opml += "<opml version=\"2.0\">\n"

  head_title = config['head']['title']
  head_dateCreated = formatDateString(config['head']['dateCreated'])
  head_dateModified = formatDateStringUTCNow()

  ownerName = config['head']['ownerName']
  ownerEmail = config['head']['ownerEmail']
  url = config['head']['url']

  opml += "  <head>\n"
  opml += f"    <title>{head_title}</title>\n"
  opml += f"    <url>{url}</url>\n"
  opml += f"    <dateCreated>{head_dateCreated} +0200</dateCreated>\n"
  opml += f"    <dateModified>{head_dateModified} +0200</dateModified>\n"
  opml += f"    <ownerName>{ownerName}</ownerName>\n"
  opml += f"    <ownerEmail>{ownerEmail}</ownerEmail>\n"
  opml += "  </head>\n"
  opml += "  <body>\n"

  for body in config['body']:
    issue_title = ""
    issue_pubDate = ""
    issue_htmlUrl = ""

    if 'title' in body:
      issue_title = body['title']

    if 'pubDate' in body:
      issue_pubDate = formatDateString(body['pubDate'])

    if 'htmlUrl' in body:
      if body['htmlUrl'] != None:
        issue_htmlUrl = body['htmlUrl']
      else:
        issue_htmlUrl = None


    if (
      (issue_title != None) and
      (issue_htmlUrl != None) and
      (issue_pubDate != None)
    ):
      opml += f"    <outline text=\"{issue_title}\" htmlUrl=\"{issue_htmlUrl}\" dateCreated=\"{issue_pubDate} +0000\">\n"
    else:
      opml += f"    <outline text=\"{issue_title}\" dateCreated=\"{issue_pubDate} +0000\">\n"

    for contents in body['contents']:
      podcast = contents['podcast']
      
      if 'type' not in podcast:
        podcast_type = "link"
      else:
        podcast_type = podcast['type']

      if 'version' not in podcast:
        podcast_version = "RSS"
      else:
        podcast_version = podcast['version']

      if 'language' not in podcast:
        podcast_language = "en"
      else:
        podcast_language = podcast['language']

      if 'title' not in podcast:
        podcast_title = ""
      else:
        podcast_title = htmlEncode(str(podcast['title']))

      if 'htmlUrl' not in podcast:
        podcast_htmlUrl = ""
      else:
        podcast_htmlUrl = htmlEncode(str(podcast['htmlUrl']))

      if 'xmlUrl' not in podcast:
        podcast_xmlUrl = ""
      else:
        podcast_xmlUrl = htmlEncode(str(podcast['xmlUrl']))

      opml += f"      <opml type=\"{podcast_type}\" version=\"{podcast_version}\" language=\"{podcast_language}\" title=\"{podcast_title}\" text=\"{podcast_title}\" htmlUrl=\"{podcast_htmlUrl}\" xmlUrl=\"{podcast_xmlUrl}\" />\n"

    opml += "    </outline>\n"

  opml += "  </body>\n"

  opml += "</opml>\n"
  
  print(opml)



def LoadYamlConfig(filepath):
  config = None
  with open(filepath, 'r') as stream:
    try:
      config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)
  return config

def main():
  config = None

  for arg in sys.argv:
    if len(arg.strip()) > 0:
      if arg != "render-opml.py":
        config = LoadYamlConfig(arg)
        ProcessItems(config)

if __name__ == '__main__':
  main()
