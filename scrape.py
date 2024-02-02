import requests
import telebot
import time
from bs4 import BeautifulSoup

req = requests.get("https://www.bbc.com/amharic")

bot_token = "6564457985:AAGkZ1CXeuE1ZoRSy-O1kM3NMOZ0vyIZjZc"
bot = telebot.TeleBot(bot_token)

def scrape_data():
    url = 'https://www.bbc.com/amharic'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all(class_="bbc-1qfus8v e5q9uf21")
    items2 = soup.find_all(class_="promo-text")
    data = []
    for i in range(min(len(items), len(items2))):
        photo_url = items[i].find("img")["src"]
        text = items2[i].find_all(class_="promo-paragraph")
        story = [s.getText() for s in text]
        link = items2[i].find("a")["href"]
        data.append((photo_url, story, link))
    return data
scrape_data()

def send_data_to_telegram_channel():
    chat_id = "456945921"
    data = scrape_data()
    for photo_url, text, link in data:
        time.sleep(5)
        bot.send_photo(chat_id, photo_url, caption=f"{text}\n\nRead More: {link}")

if __name__ == "__main__":
    send_data_to_telegram_channel()

