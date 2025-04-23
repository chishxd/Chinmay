from typing import List
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
from urllib.parse import urlparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
                  '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}
def parse_arguments():
     import argparse
     parser = argparse.ArgumentParser("Genius Scraper")
     parser.add_argument("base_url", help="Genius URL of the album to scrape lyrics from")
     return parser.parse_args()

def get_requests(base_url: str):
     """
     Description: GET's the html and parser into a BeautifulSoup object for scraping

     args: base_url : URL of the album to scrape songs
     """
     session = requests.Session()
     retry = Retry(connect=3, backoff_factor=0.5)
     adapter = HTTPAdapter(max_retries=retry)
     session.mount('http://', adapter)
     session.mount('https://', adapter)
     res = session.get(base_url, headers=headers)
     soup = BeautifulSoup(res.text, "html.parser")

     return soup

def get_songs_list(soup) -> List[str]:
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

     return url_list

def get_songs_title(soup) -> str:
     title_h1 = soup.find("h1")
     title = title_h1.get_text(strip=True) if title_h1 else "Unknown Title"
     safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).rstrip()

     return safe_title

def get_songs_lyrics(soup) -> str:
     lyrics_block = soup.find_all("span", class_="ReferentFragment-desktop__Highlight-sc-380d78dd-1 fIkrDi")
     lyrics = "\n".join([block.get_text(separator="\n").strip() for block in lyrics_block]) if lyrics_block else "----Lyrics Not Found----"

     return lyrics

def main():
     args = parse_arguments()
     url = args.base_url
     soup = get_requests(url)
     url_list = get_songs_list(soup)

     os.makedirs("lyrics_folder", exist_ok=True)

     for idx, url in enumerate(url_list, 1):
          song_soup = get_requests(url)
          title = get_songs_title(song_soup)
          lyrics = get_songs_lyrics(song_soup)

          filepath = os.path.join("lyrics_folder", f"{title}.txt")
          with open(filepath, "w", encoding='utf-8') as f:
               f.write(lyrics)
          
          print(f"[{idx}/{len(url_list)}] Saved: {title}.txt")
     
     print(f"Scraped {idx}.{len(url_list)} songs successfully.")

if __name__ == "__main__":
     main()