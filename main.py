import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://monster-book.com/front?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll({"a": "title"}):
            href = "https://monster-book.com" + str(link.get("href"))
            title = link.string
            print(title)
            print(href)
        page += 1


trade_spider(1)
