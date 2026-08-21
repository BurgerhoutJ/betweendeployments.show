import os, re, sys, html, json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
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

out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
video_feed_path = sys.argv[3] if len(sys.argv) > 3 else ""

with open(sys.argv[1], encoding="utf-8") as feed_file:
    feed_data = feed_file.read()

def parse_date(value):
    try:
        return parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)

if feed_data.lstrip().startswith("{"):
    json_feed = json.loads(feed_data)
    items = []
    for item in json_feed.get("items", []):
        enclosure = item.get("enclosure") or {}
        items.append({
            "title": item.get("title", ""),
            "pub_date": item.get("pubDate", ""),
            "link": item.get("link", ""),
            "description": item.get("content") or item.get("description", ""),
            "duration": item.get("duration", ""),
            "episode": item.get("episode", ""),
            "audio_url": enclosure.get("link", ""),
            "image_url": item.get("thumbnail", ""),
        })
else:
    channel = ET.fromstring(feed_data).find("channel")
    items = []
    for item in channel.findall("item"):
        enc = item.find("enclosure")
        ep_img = item.find("itunes:image", NS)
        items.append({
            "title": text(item, "title"),
            "pub_date": text(item, "pubDate"),
            "link": text(item, "link"),
            "description": text(item, "description"),
            "duration": text(item, "itunes:duration", NS),
            "episode": text(item, "itunes:episode", NS),
            "audio_url": enc.get("url", "") if enc is not None else "",
            "image_url": ep_img.get("href", "") if ep_img is not None else "",
        })

video_by_title = {}
if video_feed_path:
    video_root = ET.parse(video_feed_path).getroot()
    for video_entry in video_root.findall("{http://www.w3.org/2005/Atom}entry"):
        video_title = text(video_entry, "{http://www.w3.org/2005/Atom}title")
        video_link = video_entry.find("{http://www.w3.org/2005/Atom}link[@rel='alternate']")
        if video_link is not None and video_link.get("href"):
            video_by_title[video_title] = video_link.get("href")

for item in items:
    title = item["title"]
    pub_date = item["pub_date"]
    link = item["link"]
    description = item["description"]
    duration = item["duration"]
    episode = item["episode"]
    audio_url = item["audio_url"]
    image_url = item["image_url"]
    video_url = video_by_title.get(title, "")

    dt = parse_date(pub_date)
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
video: "{video_url}"
description: "{excerpt.replace('"', '\\"')}"
---

"""

    # Build post body
    body = ""
    if audio_url:
        body += f'<audio controls style="width:100%"><source src="{audio_url}" type="audio/mpeg"></audio>\n\n'
    if video_url:
        body += f'<div class="episode-video"><iframe src="{video_url.replace("watch?v=", "embed/")}" title="{title.replace(chr(34), "&quot;")}" loading="lazy" allowfullscreen></iframe></div>\n\n'
    body += html.unescape(description) + "\n\n"
    if link:
        body += f"[Listen on Substack]({link})\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(front_matter + body)

print(f"Generated {len(items)} posts in {out_dir}/")
