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


def ProcessEach():
  global config

  if config == None:
    print("config is empty")
    exit(0)

  #opml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
  #opml += "<!-- Source: https://b19.se/data/findthatpod.opml -->\n"
  #opml += "<opml version=\"2.0\">\n"

  for issue in config['body']:
    opml = []

    opml_filename = f"findthatpod-issue-{issue['issue']:03}.opml"

    opml_fullpath = f"../{opml_filename}"

    if(os.path.isfile(opml_fullpath)):
      #print(f"Skipped {opml_fullpath} - exists")
      continue

    # Declare XML
    opml.append(f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    
    # Source reference
    opml.append(f"<!-- Source: https://b19.se/data/opml/findthatpod/{opml_filename} -->")
    
    # Begin OPML
    opml.append(f"<opml version=\"2.0\">")

    # Begin head
    opml.append(f"  <head>");

    # Title
    opml.append(f"    <title>Find That Pod #{issue['issue']:03}</title>")
    
    # URL
    opml.append(f"    <url>{config['head']['url']}</url>")

    # Date created
    opml.append(f"    <dateCreated>{formatDateString(issue['pubDate'])} +0100</dateCreated>")

    # Date modified
    opml.append(f"    <dateModified>{formatDateString(issue['pubDate'])} +0100</dateModified>")

    # OwnerName
    opml.append(f"    <ownerName>{htmlEncode(config['head']['ownerName'])}</ownerName>")

    # OwnerEmail
    opml.append(f"    <ownerEmail>{htmlEncode(config['head']['ownerEmail'])}</ownerEmail>")

    # End head
    opml.append(f"  </head>");

    # Begin body
    opml.append(f"  <body>");


    file_creation_time = f"{formatDateString(issue['pubDate'])} +0100"
    file_ctime = int( datetime.strptime(file_creation_time, '%a, %d %b %Y %H:%M:%S %z').timestamp() )

    if issue['htmlUrl'] != None:
      opml.append(f"    <outline text=\"Find That Pod #{issue['issue']:03}\" htmlUrl=\"{htmlEncode(issue['htmlUrl'])}\" dateCreated=\"{formatDateString(issue['pubDate'])} +0100\">")
    else:
      opml.append(f"    <outline text=\"Find That Pod #{issue['issue']:03}\" dateCreated=\"{formatDateString(issue['pubDate'])} +0100\">")

    # Items
    for item in issue['contents']:
      podcast = item['podcast']
      opml.append(f"      <outline type=\"link\" version=\"RSS\" language=\"en\" title=\"{htmlEncode(podcast['title'])}\" text=\"{htmlEncode(podcast['title'])}\" htmlUrl=\"{htmlEncode(podcast['htmlUrl'])}\" xmlUrl=\"{htmlEncode(podcast['xmlUrl'])}\" />")

    # end outline
    opml.append(f"    </outline>")

    # enn body
    opml.append(f"  </body>");

    # end OPML
    opml.append(f"</opml>");

    opml_rendered = "\n".join(opml)

    with open(opml_fullpath, "w") as f:
      f.write(opml_rendered)

    # Adjust creation/modified time to episode pubDate
    os.utime(opml_fullpath, (file_ctime, file_ctime))


def ProcessItems():
  global config

  utc_now = datetime.now().isoformat()

  if config == None:
    print("config is empty")
    exit(0)

  opml = []
  opml.append(f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
  opml.append(f"<!-- Source: https://b19.se/data/findthatpod/findthatpod.opml -->")
  opml.append(f"<opml version=\"2.0\">")

  head_title = config['head']['title']
  head_dateCreated = formatDateString(config['head']['dateCreated'])
  head_dateModified = formatDateStringUTCNow()

  ownerName = config['head']['ownerName']
  ownerEmail = config['head']['ownerEmail']
  url = config['head']['url']

  opml.append(f"  <head>")
  opml.append(f"    <title>{head_title}</title>")
  opml.append(f"    <url>{url}</url>")
  opml.append(f"    <dateCreated>{head_dateCreated} +0100</dateCreated>")
  opml.append(f"    <dateModified>{head_dateModified} +0100</dateModified>")
  opml.append(f"    <ownerName>{ownerName}</ownerName>")
  opml.append(f"    <ownerEmail>{ownerEmail}</ownerEmail>")
  opml.append(f"  </head>")
  opml.append(f"  <body>")

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
      opml.append(f"    <outline text=\"{issue_title}\" htmlUrl=\"{issue_htmlUrl}\" dateCreated=\"{issue_pubDate} +0000\">")
    else:
      opml.append(f"    <outline text=\"{issue_title}\" dateCreated=\"{issue_pubDate} +0000\">")

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

      opml.append(f"      <opml type=\"{podcast_type}\" version=\"{podcast_version}\" language=\"{podcast_language}\" title=\"{podcast_title}\" text=\"{podcast_title}\" htmlUrl=\"{podcast_htmlUrl}\" xmlUrl=\"{podcast_xmlUrl}\" />")

    opml.append(f"    </outline>")

  opml.append(f"  </body>")

  opml.append(f"</opml>")
  
  opml_rendered = "\n".join(opml)

  with open(OUTPUT_FILENAME, "w") as f:
    f.write(opml_rendered)

  return



def LoadYamlConfig(filepath):
  global config
  with open(filepath, 'r') as stream:
    try:
      config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)


def main():
  global config
  config = None

  LoadYamlConfig(SOURCE_YAML)
  ProcessItems()
  ProcessEach()

if __name__ == '__main__':
  main()
