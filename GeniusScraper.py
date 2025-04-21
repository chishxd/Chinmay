import requests
from bs4 import BeautifulSoup

url = "https://genius.com/albums/The-weeknd/House-of-balloons"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://genius.com/albums/The-weeknd/House-of-balloons")
html = response.text

soup = BeautifulSoup(html, "html.parser")

songs_list = soup.find_all("a", class_="u-display_block", href=True)

url_list = []
for song in songs_list:
    href = song["href"] # type: ignore[]
    if "The-weeknd" in href and 'lyrics' in href:
        url_list.append(href)

for url in url_list:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    lyrics_a = soup.find_all('a', class_="ReferentFragment-desktop__ClickTarget-sc-380d78dd-0 jCKWLY")
    lyrics_span = soup.find_all('span', class_="ReferentFragment-desktop__Highlight-sc-380d78dd-1 fIkrDi")

    title_h1 = soup.find('h1', class_ = 'SongHeaderV3-desktop__Title-sc-12378ce7-9 iHGygD')
    if title_h1 is not None:
        span = title_h1.find('span', class_="SongHeaderV3-desktop__HiddenMask-sc-12378ce7-13 cAUebg") #type:ignore
        if span is not None:
            print(f"----{span.get_text()}----")
            print()
        else:
            print("Span not found inside h1")
    else:
        print("Title Not Found")
        print()

    if lyrics_span:
        for lyrics in lyrics_span:
            print(lyrics.get_text("\n").strip())
            print()
