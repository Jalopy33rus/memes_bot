import requests
from bs4 import BeautifulSoup

def get_memes(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('entry')
    memes = []
    for item in items[:5]:
        link = item.link['href']
        title = item.title.text
        memes.append({'title': title, 'link': link})
    return memes
