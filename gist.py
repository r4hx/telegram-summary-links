import logging
import os
import threading
import time

import httpx

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
assert GITHUB_TOKEN, "GITHUB_TOKEN is not set"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


def get_raw_gist_url_from_text(text: str):
    data = {
        "description": "Temporary gist for 300.yandex.ru",
        "public": False,
        "files": {"temp_file.txt": {"content": text}},
    }

    response = httpx.post(
        "https://api.github.com/gists",
        headers=headers,
        json=data,
    )

    if response.status_code == 201:
        gist_data = response.json()
        gist_id = gist_data["id"]
        raw_url = gist_data["files"]["temp_file.txt"]["raw_url"]
        logging.info(f"Gist создан: {gist_data["html_url"]}")
        logging.info(f"Raw URL: {raw_url}")
        return {"gist_id": gist_id, "raw_url": raw_url}
    else:
        logging.error(
            f"Ошибка при создании gist: {response.status_code} - {response.json()}",
        )
        raise Exception("Ошибка при создании gist")


def delete_gist(gist_id: str):
    time.sleep(30)
    delete_response = httpx.delete(
        f"https://api.github.com/gists/{gist_id}",
        headers=headers,
    )
    if delete_response.status_code == 204:
        logging.info("Gist удалён.")
    else:
        logging.error(
            f"Ошибка при удалении gist: {delete_response.status_code} - {delete_response.json()}",
        )


def delete_gist_in_background(gist_id: str):
    thread = threading.Thread(target=delete_gist, args=(gist_id,))
    thread.start()
