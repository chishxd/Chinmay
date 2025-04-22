#import packages
import requests #to get html of site
from bs4 import BeautifulSoup #to parse the html
import os #to make folder
from urllib.parse import urlparse #to parse url for it's path
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


base_url = "https://genius.com/albums/The-weeknd/Hurry-up-tomorrow"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
                  '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

#Credit : https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
res = session.get(base_url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
songs_list = soup.find_all('a', class_= "u-display_block")

seen = set()
url_list = []

for song in songs_list:
    href = song["href"]
    if href.endswith("-lyrics"):
        path = urlparse(href).path.lower()
        if path not in seen:
            seen.add(path)
            url_list.append(href)

os.makedirs("lyrics_output", exist_ok=True)

for idx, url in enumerate(url_list, 1):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    title_h1 = soup.find("h1")
    title = title_h1.get_text(strip=True) if title_h1 else f"Track_{idx}"
    safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).rstrip()

    lyrics_block = soup.find_all("span", class_="ReferentFragment-desktop__Highlight-sc-380d78dd-1 fIkrDi")
    lyrics = "\n".join([block.get_text(separator="\n").strip() for block in lyrics_block]) if lyrics_block else "----Lyrics Not Found----"

    filepath = os.path.join("lyrics_output", f"{idx}.{safe_title}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(lyrics)

    print(f"[{idx}/{len(url_list)}] Saved: {safe_title}.txt")

print(f"Saved {len(url_list)} songs to ./lyrics_output")
