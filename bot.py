import json
import schedule
import time
from telegram import Bot
from news_parser import get_news
from meme_parser import get_memes

# Загружаем конфиг
with open("config.json", "r") as f:
    config = json.load(f)

bot = Bot(token=config['telegram_token'])
chat_id = config['chat_id']

def send_news_and_memes():
    # Новости
    for url in config['news_sources']:
        news_list = get_news(url)
        for news in news_list:
            msg = f"📰 {news['title']}\n{news['link']}"
            bot.send_message(chat_id=chat_id, text=msg)
    
    # Мемы
    for url in config['meme_sources']:
        memes = get_memes(url)
        for meme in memes:
            msg = f"😂 {meme['title']}\n{meme['link']}"
            bot.send_message(chat_id=chat_id, text=msg)

# Запускаем сбор каждые 60 минут
schedule.every(60).minutes.do(send_news_and_memes)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(10)
