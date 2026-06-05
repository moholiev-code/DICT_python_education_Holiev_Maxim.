import os
import string

import requests
from bs4 import BeautifulSoup


def create_filename(title):

    filename = title.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    filename = filename.replace(" ", "_")

    return filename


pages = int(input())
article_type_needed = input()

headers = {
    "Accept-Language": "en-US,en;q=0.5"
}

base_url = (
    "https://www.nature.com/nature/articles"
    "?sort=PubDate&year=2022&page="
)

for page_number in range(1, pages + 1):

    folder_name = f"Page_{page_number}"

    os.makedirs(folder_name, exist_ok=True)

    url = base_url + str(page_number)

    response = requests.get(
        url,
        headers=headers
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    articles = soup.find_all("article")

    for article in articles:

        article_type = article.find(
            "span",
            {"data-test": "article.type"}
        )

        if not article_type:
            continue

        if article_type.text.strip() != article_type_needed:
            continue

        article_link = article.find(
            "a",
            {"data-track-action": "view article"}
        )

        if not article_link:
            continue

        article_title = article_link.text.strip()

        article_url = (
            "https://www.nature.com"
            + article_link.get("href")
        )

        article_response = requests.get(
            article_url,
            headers=headers
        )

        article_soup = BeautifulSoup(
            article_response.text,
            "html.parser"
        )

        body = article_soup.find(
            "div",
            class_=lambda value:
            value and "body" in value
        )

        if body is None:

            body = article_soup.find("article")

        if body is None:
            continue

        article_text = body.get_text(
            separator="\n",
            strip=True
        )

        filename = create_filename(
            article_title
        )

        filepath = os.path.join(
            folder_name,
            f"{filename}.txt"
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(article_text)

print("Saved all articles.")