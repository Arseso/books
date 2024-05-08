INIT_TABLE_BOOKS= """
    CREATE TABLE IF NOT EXISTS Books (
    id int PRIMARY KEY,
    creator_id int NOT NULL,
    permission varchar(7) NOT NULL,
    author int NOT NULL,
    book_name varchar(100),
    src varchar(50),
    image_src varchar(100),
    last_update timestamp NOT NULL
);"""

INIT_TABLE_USERS = """
    CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY DEFAULT 0,
    nickname varchar(50) NOT NULL,
    passwd varchar(50) NOT NULL,
    role varchar(5) NOT NULL,
    token character varying(5)[] COLLATE pg_catalog."default" NOT NULL;
);"""

# books requests
GET_BOOK_CREATOR_ID = """
    SELECT creator_id FROM Books
    WHERE id = {}
;"""


GET_BOOKS_USER = """
    SELECT creator_id, permission, author,
    book_name, src, image_src, price, pages, id, last_update FROM Books 
    WHERE creator_id = {user_id} OR permission = 'public'
;"""

GET_BOOKS_ADM = """
    SELECT creator_id, permission, author,
    book_name, src, image_src, price, pages, id, last_update FROM Books 
;"""

ADD_BOOK = """
    INSERT INTO books (creator_id, permission, author, book_name, src, image_src, price, pages)
    VALUES ({}, '{}', '{}', '{}', '{}', '{}', {}, {})
;"""

UPD_BOOK = """
    UPDATE books
    SET creator_id = {}, permission = '{}', author = '{}',
    book_name = '{}', src = '{}', image_src = '{}', price = {}, pages = {}
    WHERE id = {}
;"""

DEL_BOOK = """
DELETE FROM books
WHERE id = {}"""

GET_BOOKS_UPDATE_USER = """
    SELECT creator_id, permission, author,
    book_name, src, image_src, price, pages, id, last_update FROM Books 
    WHERE (creator_id = {user_id} OR permission = 'public') AND last_update > '{}'
;"""

GET_BOOKS_UPDATE_ADM = """
    SELECT creator_id, permission, author,
    book_name, src, image_src, price, pages, id, last_update FROM Books 
    WHERE last_update > '{}'
;"""

# users requests

SET_NEW_USER = """
    INSERT INTO users (nickname, passwd, token) VALUES
    ('{nick}', '{passwd}', '{token}');
"""

GET_USER_TOKEN = """
    SELECT token FROM users
    WHERE nickname = '{nick}' and passwd = '{passwd}';
"""

GET_USER_ROLE = """
    SELECT role FROM users
    WHERE token = '{token}';
"""

SET_USER_ROLE = """
UPDATE users
SET role = '{role}'
WHERE token = '{token}';
"""

DEL_USER = """
    DELETE FROM users
    WHERE token = '{token}'
;"""

GET_USER_ID = """
    SELECT id FROM users
    WHERE token = '{token}'
;"""





