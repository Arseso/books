import re
from typing import List, Any

from server.data.books import Book
from server.data.requests import execute_set_request as db_set
import server.data.requests_library as lib
from bs4 import BeautifulSoup as bs, ResultSet, BeautifulSoup
import requests as req
import server.data.collecting.const as c




def db_add(*args) -> None:
    return db_set(lib.ADD_BOOK.format(*args))


def get_page(src: str) -> BeautifulSoup:
    page = bs(req.get(url=src, headers=c.headers).text, 'html5lib')
    return page


def get_authors(a: bs) -> str:
    authors = ""
    for name in a('a'):
        authors += f", {name['title']}"
    return authors[2:]


def get_float(price: str):
    price_cleaned = price.replace('\u2009', '').replace('\xa0', '').replace('₽', '')
    return float(price_cleaned)


def get_pages(source: str) -> int:
    page = get_page(source)
    text = page('div', {'class': c.DIV_PAGES_CLASS})
    try:
        text = text[0].text
    except IndexError:
        return -1

    return int(re.search(r"Страниц: (\d+)", text).group(1))


def parse_books(source: str) -> None:
    page = get_page(source)
    titles = [a['title'] for a in page('a', {'class': c.A_TITLE_CLASS})]
    authors = [get_authors(a) for a in page('div', {'class': c.DIV_AUTHOR_CLASS})]
    sources = [c.PAGE_HOME + a['href'] for a in page('a', {'class': c.A_TITLE_CLASS})]
    img_sources = [a['data-src'] for a in page('img', {'class': c.IMG_CLASS})]
    costs = [get_float(a.text.strip()) for a in page('div', {'class': c.DIV_PRICE_CLASS})]
    pages = [get_pages(source) for source in sources]
    if len(titles) == len(authors) == len(sources) == len(img_sources) == len(costs) == len(pages):
        print("Equal")

    for i in range(len(sources)):
        print(sources[i])
        db_add(4, "public", authors[i], titles[i], sources[i], img_sources[i], costs[i], pages[i])

