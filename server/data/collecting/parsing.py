import re
from typing import List, Any

from server.data.books import Book
from server.data.requests import execute_set_request as db_set
import server.data.requests_library as lib
from bs4 import BeautifulSoup as bs, ResultSet, BeautifulSoup
import requests as req
import server.data.collecting.const as c


def db_add(book: Book) -> None:
    return db_set(lib.ADD_BOOK.format(*book.get_params()))


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


def parse_book_from_div(div: bs) -> None:
    try:
        title = div('a', {'class': c.A_TITLE_CLASS})[0]['title']
        author = get_authors(div('div', {'class': c.DIV_AUTHOR_CLASS})[0])
        src = c.PAGE_HOME + div('a', {'class': c.A_TITLE_CLASS})[0]['href']
        img_src = div('img', {'class': c.IMG_CLASS})[0]['data-src']
        price = get_float(div('div', {'class': c.DIV_PRICE_CLASS})[0].text)
        pages = get_pages(src)
    except IndexError:
        print(f"Error while parsing book")
        return None
    db_add(Book(creator_id=4, permission="public", book_name=title, author=author, src=src, price=price, pages=pages,
                image_src=img_src))
    return None


def parse_book_divs(source: str) -> None:
    page = get_page(source)
    for div in page('div', {'class': c.DIV_BOOK_BLOCK_CLASS}):
        parse_book_from_div(div)
