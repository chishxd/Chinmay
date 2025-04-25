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
    """
    Parses command-line arguments for the script.

    Returns:
        argparse.Namespace: Parsed arguments containing the 'base_url' of the album to scrape lyrics from.
    """
    import argparse
    parser = argparse.ArgumentParser("Genius Scraper")
    parser.add_argument("base_url", help="Genius URL of the album to scrape lyrics from")
    return parser.parse_args()

def get_requests(base_url: str):
    """
    Sends an HTTP GET request to the given URL and returns a BeautifulSoup object for parsing.

    Args:
        base_url (str): URL of the album to scrape songs from.

    Returns:
        BeautifulSoup: Parsed HTML content of the requested page.
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
    """
    Extracts and returns a list of unique song URLs from the album page.

    Args:
        soup (BeautifulSoup): Parsed HTML content of the album page.

    Returns:
        List[str]: List of URLs for individual songs ending with "-lyrics".
    """
    songs_list = soup.find_all('a', class_="u-display_block")
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
    """
    Extracts and sanitizes the title of a song from the parsed HTML content.

    Args:
        soup (BeautifulSoup): Parsed HTML content of the song page.

    Returns:
        str: Sanitized title of the song. Returns "Unknown Title" if the title cannot be found.
    """
    title_h1 = soup.find("h1")
    title = title_h1.get_text(strip=True) if title_h1 else "Unknown Title"
    safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).rstrip()

    return safe_title

def get_songs_lyrics(soup) -> str:
    """
    Extracts the lyrics of a song from the parsed HTML content.

    Args:
        soup (BeautifulSoup): Parsed HTML content of the song page.

    Returns:
        str: Lyrics of the song. Returns "----Lyrics Not Found----" if the lyrics cannot be found.
    """
    lyrics_block = soup.find_all("span", class_="ReferentFragment-desktop__Highlight-sc-380d78dd-1 fIkrDi")
    lyrics = "\n".join([block.get_text(separator="\n").strip() for block in lyrics_block]) if lyrics_block else "----Lyrics Not Found----"

    return lyrics

def main():
    """
    Main function for the Genius Scraper script.

    - Parses command-line arguments to get the base URL of the album.
    - Scrapes the album page for song links, titles, and lyrics.
    - Saves the lyrics of each song to a text file in the 'lyrics_folder' directory.
    - Prints the progress and summary of the scraping process.
    """
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
    
    print(f"Scraped {idx}/{len(url_list)} songs successfully.")

if __name__ == "__main__":
    main()