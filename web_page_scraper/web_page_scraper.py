import os
import string

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={}"

headers = {
    "Accept-Language": "en-US,en;q=0.5"
}


def create_filename(title):
    translator = str.maketrans("", "", string.punctuation)

    filename = title.translate(translator)
    filename = filename.replace(" ", "_")
    filename = filename.replace("—", "")
    filename = filename.replace("–", "")

    return filename + ".txt"


pages = int(input())
article_type_needed = input()

for page_number in range(1, pages + 1):

    folder_name = f"Page_{page_number}"
    os.makedirs(folder_name, exist_ok=True)

    response = requests.get(
        BASE_URL.format(page_number),
        headers=headers
    )

    if response.status_code != 200:
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    for article in soup.find_all("article"):

        article_type = article.find(
            "span",
            {"data-test": "article.type"}
        )

        if article_type is None:
            continue

        if article_type.text.strip() != article_type_needed:
            continue

        article_link = article.find(
            "a",
            {"data-track-action": "view article"}
        )

        if article_link is None:
            continue

        article_title = article_link.text.strip()

        article_url = (
            "https://www.nature.com"
            + article_link["href"]
        )

        article_response = requests.get(
            article_url,
            headers=headers
        )

        if article_response.status_code != 200:
            continue

        article_soup = BeautifulSoup(
            article_response.text,
            "html.parser"
        )

        body = article_soup.find(
            "div",
            class_=lambda value: value and "body" in value
        )

        if body is None:
            continue

        article_text = "\n".join(body.stripped_strings)

        file_name = create_filename(article_title)

        file_path = os.path.join(
            folder_name,
            file_name
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(article_text)

print("Saved all articles.")