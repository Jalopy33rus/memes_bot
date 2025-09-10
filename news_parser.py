import requests
from bs4 import BeautifulSoup

def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    news_list = []
    for item in items[:5]:  # берём 5 последних новостей
        news_list.append({
            'title': item.title.text,
            'link': item.link.text
        })
    return news_list
