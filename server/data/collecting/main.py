from server.data.collecting.parsing import parse_book_divs

PAGES = [
    "https://www.labirint.ru/search/python/?stype=0&page=1",
    "https://www.labirint.ru/search/python/?stype=0&page=2",
    "https://www.labirint.ru/search/python/?stype=0&page=3",
    "https://www.labirint.ru/search/python/?stype=0&page=4",
]


def main():
    for page in PAGES:
        parse_book_divs(page)
        print(f"{page} append to db")


if __name__ == '__main__':
    main()
