# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
import json as json_lib


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    root = ET.fromstring(xml)
    channel = root.find("channel")
    if channel is None:
        raise ValueError("Invalid RSS feed: Missing <channel> element.")

    result = []
    channel_info = {
        "title": channel.findtext("title"),
        "link": channel.findtext("link"),
        "lastBuildDate": channel.findtext("lastBuildDate"),
        "pubDate": channel.findtext("pubDate"),
        "language": channel.findtext("language"),
        "category": [category.text for category in channel.findall("category") if category.text],
        "editor": channel.findtext("managingEditor"),
        "description": channel.findtext("description"),
        "items": [],
    }

    for item in channel.findall("item"):
        item_info = {
            "title": item.findtext("title"),
            "author": item.findtext("author"),
            "pubDate": item.findtext("pubDate"),
            "link": item.findtext("link"),
            "category": [category.text for category in item.findall("category") if category.text],
            "description": item.findtext("description"),
        }
        if item_info["title"] or item_info["description"]:
            channel_info["items"].append(item_info)

    if limit is not None:
        channel_info["items"] = channel_info["items"][:limit]

    if json:
        return [json_lib.dumps({k: v for k, v in channel_info.items() if v}, indent=2)]

    result.append(f"Feed: {channel_info['title']}")
    result.append(f"Link: {channel_info['link']}")
    if channel_info.get("lastBuildDate"):
        result.append(f"Last Build Date: {channel_info['lastBuildDate']}")
    if channel_info.get("pubDate"):
        result.append(f"Publish Date: {channel_info['pubDate']}")
    if channel_info.get("language"):
        result.append(f"Language: {channel_info['language']}")
    if channel_info.get("category"):
        result.append(f"Categories: {', '.join(channel_info['category'])}")
    if channel_info.get("editor"):
        result.append(f"Editor: {channel_info['editor']}")
    if channel_info.get("description"):
        result.append(f"Description: {channel_info['description']}")
    result.append("")

    for item in channel_info["items"]:
        result.append(f"Title: {item['title']}" if item.get("title") else "")
        if item.get("author"):
            result.append(f"Author: {item['author']}")
        if item.get("pubDate"):
            result.append(f"Published: {item['pubDate']}")
        if item.get("link"):
            result.append(f"Link: {item['link']}")
        if item.get("category"):
            result.append(f"Categories: {', '.join(item['category'])}")
        if item.get("description"):
            result.append("")
            result.append(f"{item['description']}")
        result.append("")

    return [line for line in result if line]


def main(argv: Optional[Sequence] = None):
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()