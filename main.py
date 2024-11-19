import logging
import os
import re
from time import sleep

import telebot

from gist import delete_gist_in_background, get_raw_gist_url_from_text
from yandex import get_summary_from_yandex, send_url_to_yandex
from youtube import extract_video_id, get_video_transcript

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
            result_link = is_youtube_link(link)
            url = send_url_to_yandex(result_link)
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


def is_youtube_link(link):
    if re.match(r"(https?://)?(www\.)?youtube\.com/", link):
        url = create_gist_for_youtube_link(link)
        delete_gist_in_background(gist_id=url["gist_id"])
        return url["raw_url"]
    elif re.match(r"(https?://)?(www\.)?youtu\.be/", link):
        url = create_gist_for_youtube_link(link)
        delete_gist_in_background(gist_id=url["gist_id"])
        return url["raw_url"]
    else:
        return link


def create_gist_for_youtube_link(link):
    video_id = extract_video_id(link)
    transcript = get_video_transcript(video_id)
    result = get_raw_gist_url_from_text(transcript)
    return result


bot.polling(non_stop=True)
