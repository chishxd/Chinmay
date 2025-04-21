import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

# Setup
base_url = "https://genius.com/albums/The-weeknd/House-of-balloons"
headers = {'User-Agent': 'Mozilla/5.0'}

# Step 1: Get song URLs from album page
response = requests.get(base_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
songs_list = soup.find_all("a", class_="u-display_block", href=True)

seen = set()
url_list = []

for song in songs_list:
    href = song["href"] # type: ignore[]
    if href.endswith("-lyrics"): # type: ignore[]
        #parses url for path in URL. eg. in https://genius.com/The-weeknd-high-for-this-lyrics, The-weeknd-high-for-this-lyrics is path
        path = urlparse(href).path.lower() # type: ignore[]
        #Checks if the path is in the set. If it isn't then add the path to set and link to url_list
        if path not in seen:
            seen.add(path)
            url_list.append(href)
# Verify total count of songs in album
print(f"Found {len(url_list)} unique song URLs.")
if len(url_list) != 9:
    print("⚠️ Warning: Expected 9 songs. You might be missing one or have extras.")

# Creates output dir, exist_ok ensure that no exceptions are thrown if directory already exists
os.makedirs("lyrics_output", exist_ok=True)

#Scrape lyrics and save each song in it's own .txt file
for idx, url in enumerate(url_list, 1): #loops through each url in url_list start from idx(index) 1
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # Extract title
    title_h1 = soup.find('h1')
    title = title_h1.get_text(strip=True) if title_h1 else f"track_{idx}"
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_', '-')).rstrip() #removes any alphanumeric character, symbol or whitespace in title

    # Extract lyrics
    lyrics_blocks = soup.find_all('span', class_="ReferentFragment-desktop__Highlight-sc-380d78dd-1 fIkrDi")
    lyrics = "\n".join([block.get_text(separator="\n").strip() for block in lyrics_blocks]) if lyrics_blocks else "----Lyrics Not Found----"
    # ^ This line joins each stanza in song by adding "\n" hence making a single string text

    # Save to text file
    filepath = os.path.join("lyrics_output", f"{safe_title}.txt") #makes a filepath by adding / in between each argument. eg.lyrics/High For This.txt
    with open(filepath, "w", encoding="utf-8") as f: #writes the lyrics string made at line 47 in file at filepath specified above
        f.write(lyrics)

    print(f"[{idx}/{len(url_list)}] Saved: {safe_title}.txt") #display scraping process

print("\n✅ DONE. Lyrics saved to ./lyrics_output/")#Confirm successful scraping

