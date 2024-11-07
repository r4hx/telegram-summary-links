import logging
import os

import httpx
from bs4 import BeautifulSoup

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

YANDEX_ENDPOINT = os.getenv("YANDEX_ENDPOINT")
assert YANDEX_ENDPOINT, "YANDEX_ENDPOINT is not set"
YANDEX_TOKEN = os.getenv("YANDEX_TOKEN")
assert YANDEX_TOKEN, "YANDEX_TOKEN is not set"

http = httpx.Client(timeout=15, follow_redirects=True)


def send_url_to_yandex(url: str) -> str:
    response = http.post(
        url=YANDEX_ENDPOINT,
        json={"article_url": url},
        headers={"Authorization": f"OAuth {YANDEX_TOKEN}"},
    )

    if response.status_code != 200:
        raise Exception("Не удалось отправить ссылку на статью в Яндекс 300")

    sharing_url = response.json().get("sharing_url")
    if not sharing_url:
        raise Exception("Не удалось получить ссылку на статью в Яндекс 300")

    return sharing_url


def get_summary_from_yandex(url: str) -> dict:
    response = http.get(url=url)

    if response.status_code != 200:
        raise Exception("Не удалось получить пересказ статьи из Яндекс 300")

    description = extract_summary(response.text)

    return description


def extract_summary(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "html.parser")
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag and "content" in meta_tag.attrs:
        return str(" " + meta_tag.get("content"))
    else:
        raise Exception("Не удалось извлечь описание статьи")
