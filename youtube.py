from bs4 import BeautifulSoup
import os
import requests
from platform import system
if system() != 'Windows':
    vlc = 'vlc'
else:
    vlc = r'C:\Program Files (x86)\VideoLAN\VLC\vlc'

query = input("what to search: ")
raw = requests.get("https://www.youtube.com/results?search_query={}".format(query))

html = raw.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.findAll("a", {"class":
                            lambda x: x and
                            'yt-uix-tile-link' in x.split()}, href=True)

i = 0
for f in titles:
    if not f.get("href").startswith("/watch"):
        titles.pop(i)
    i += 1

i = 0
for f in titles:
    title = f.get("title")
    print("({}) {}".format(i,title))
    i += 1

i = input("which to watch: ")
if not isinstance(i,str):
    i = int(i)

    cmd = '"'+vlc+'"'+" https://www.youtube.com{}".format(titles[i].get("href"))
    os.system(cmd)
