import requests
from tqdm import tqdm
import time
import urllib.parse
import urllib
import os

file = "links.txt"

with open(file, "r") as f:
    links = f.read().splitlines()
    ### Previous Method will incorporate new lines "\n" which you don't want for a URL  This will remove that

path = "./download/"

if not os.path.exists(path):
    os.makedirs(path)
    ### this will help if path doesn't already exist like I didnt' have

for piece in links:
    response = requests.get(piece, stream=True)
    urlpiece = piece.split("/")
    name = urlpiece[len(urlpiece)-1]
    name = urllib.parse.unquote(name)
    total_size = int(response.headers.get('content-length', 0))
    bs = 1024
    progress = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(path + name, 'wb') as f:
        for data in response.iter_content(bs):
         progress.update(len(data))
         f.write(data)
    progress.close()
    if total_size != 0 and progress.n != total_size:
        'print' "Error - ", name

    time.sleep(2)