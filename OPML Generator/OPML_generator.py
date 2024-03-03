#!/usr/bin/python3
import argparse
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

#Parser
parser = argparse.ArgumentParser(description='Convert RSS links into a OPML-formatted XML document')
parser.add_argument('file',type=argparse.FileType('r'), help='input file')
args = parser.parse_args()

#RSS formatting
root = ET.Element("opml", xmlns="http://www.w3.org/1999/xhtml")
head = ET.SubElement(root, "head")
body = ET.SubElement(root, "body")
outline = ET.SubElement(body, "outline", text="feeds")
#Title
ET.SubElement(head, "title").text = "Podcast Feed"

def text_to_rss():
    lines = args.file.readlines()
    for line in lines:
        url = line.strip()
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, features="xml")
        # We only need the first title, link, and description
        title = soup.find('title').get_text()
        link = soup.find('link').get_text()
        desc = soup.find('description').get_text()
        ET.SubElement(outline, "outline", type="rss", text=title.strip(), description=desc, xmlUrl=url)

text_to_rss()
tree = ET.ElementTree(root)
tree.write("output.xml")
