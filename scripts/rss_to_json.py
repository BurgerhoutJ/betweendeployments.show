import json, sys, xml.etree.ElementTree as ET

NS = {
    "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
    "content": "http://purl.org/rss/1.0/modules/content/",
}

def text(el, tag, ns=None):
    child = el.find(tag, ns) if ns else el.find(tag)
    return child.text.strip() if child is not None and child.text else ""

tree = ET.parse(sys.argv[1])
channel = tree.getroot().find("channel")

show = {
    "title": text(channel, "title"),
    "description": text(channel, "description"),
    "link": text(channel, "link"),
    "image": "",
}
img = channel.find("itunes:image", NS)
if img is not None:
    show["image"] = img.get("href", "")

episodes = []
for item in channel.findall("item"):
    enc = item.find("enclosure")
    ep = {
        "title": text(item, "title"),
        "description": text(item, "description"),
        "pubDate": text(item, "pubDate"),
        "link": text(item, "link"),
        "audio": enc.get("url", "") if enc is not None else "",
        "duration": text(item, "itunes:duration", NS),
        "episode": text(item, "itunes:episode", NS),
        "image": "",
    }
    ep_img = item.find("itunes:image", NS)
    if ep_img is not None:
        ep["image"] = ep_img.get("href", "")
    episodes.append(ep)

with open(sys.argv[2], "w", encoding="utf-8") as f:
    json.dump({"show": show, "episodes": episodes}, f, ensure_ascii=False, indent=2)
