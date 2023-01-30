import argparse
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


def find_files(url):
    url_stem = url.rsplit("/", 1)[0] + "/"
    soup = BeautifulSoup(requests.get(url_stem).text, "html.parser")

    hrefs = []

    for a in soup.find_all("a"):
        hrefs.append(a["href"])

    return hrefs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape links from a webpage")
    parser.add_argument("url", help="The URL to scrape")
    args = parser.parse_args()

    url_stem = args.url.rsplit("/", 1)[0] + "/"

    list_of_links = find_files(url_stem)

    # output_dir = os.environ.get("OUTPUT_DIR", "output")
    # filename = os.path.join(output_dir, "urls.txt")
    filename = "urls.txt"
    with open(filename, "w") as f:
        for link in list_of_links:
            if "html" in link and "#" not in link:
                f.write(url_stem + link + "\n")

    print("Links saved to urls.txt")
