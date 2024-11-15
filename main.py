import logging
import os
import re
from time import sleep

import telebot

from yandex import get_summary_from_yandex, send_url_to_yandex

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")

assert TELEGRAM_TOKEN, "TELEGRAM_TOKEN is not set"
assert TELEGRAM_GROUP_ID, "TELEGRAM_GROUP_ID is not set"

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(
    func=lambda message: bool(re.search(r"https?://", message.text)),
)
def handle_links(message):
    links = re.findall(r"https?://\S+", message.text)
    for link in links:
        try:
            url = send_url_to_yandex(link)
            for _ in range(10):
                try:
                    text = get_summary_from_yandex(url)
                    if text:
                        bot.reply_to(message, text)
                        break
                except Exception:
                    sleep(5)
        except Exception as e:
            logging.error(f"Error: {e}")


bot.polling(non_stop=True)
