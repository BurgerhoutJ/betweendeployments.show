import os, re, sys, html
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

NS = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}

def slug(title):
    s = title.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"[\s_]+", "-", s)[:80].strip("-")

def text(el, tag, ns=None):
    child = el.find(tag, ns) if ns else el.find(tag)
    return child.text.strip() if child is not None and child.text else ""

def strip_html(raw):
    return re.sub(r"<[^>]+>", "", html.unescape(raw))

tree = ET.parse(sys.argv[1])
out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)

channel = tree.getroot().find("channel")

for item in channel.findall("item"):
    title = text(item, "title")
    pub_date = text(item, "pubDate")
    link = text(item, "link")
    description = text(item, "description")
    duration = text(item, "itunes:duration", NS)
    episode = text(item, "itunes:episode", NS)

    enc = item.find("enclosure")
    audio_url = enc.get("url", "") if enc is not None else ""

    ep_img = item.find("itunes:image", NS)
    image_url = ep_img.get("href", "") if ep_img is not None else ""

    dt = parsedate_to_datetime(pub_date)
    date_str = dt.strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug(title)}.md"
    filepath = os.path.join(out_dir, filename)

    excerpt = strip_html(description)[:200].rsplit(" ", 1)[0] + "..."

    front_matter = f"""---
layout: post
title: "{title.replace('"', '\\"')}"
author: jeroen
categories: [Podcast]
tags: [intune, modern-workplace]
image: "{image_url}"
date: {dt.strftime("%Y-%m-%d %H:%M:%S %z")}
audio: "{audio_url}"
duration: "{duration}"
episode: "{episode}"
link: "{link}"
description: "{excerpt.replace('"', '\\"')}"
---

"""

    # Build post body
    body = ""
    if audio_url:
        body += f'<audio controls style="width:100%"><source src="{audio_url}" type="audio/mpeg"></audio>\n\n'
    body += html.unescape(description) + "\n\n"
    if link:
        body += f"[Listen on Substack]({link})\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(front_matter + body)

print(f"Generated {len(channel.findall('item'))} posts in {out_dir}/")
