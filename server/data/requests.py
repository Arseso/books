import psycopg2 as pg
import server.data.requests_library as lib
from server.config import DB_AUTOCOMMIT, DB_HOST, DB_USER, DB_PASSWD, DB_NAME, DB_PORT
from server.core.logs import print_database_created_connection, print_database_get_request_completed, \
    print_database_set_request_completed, print_database_closed_connection

conn, cur = None, None


def conn_cur_init() -> None:
    global conn, cur
    conn = pg.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWD,
        database=DB_NAME)
    cur = conn.cursor()
    conn.autocommit = DB_AUTOCOMMIT
    print_database_created_connection(DB_NAME, DB_HOST, DB_PORT)

def con_cur_close() -> None:
    global cur, conn
    if conn is not None:
        cur.close()
        conn.close()
        print_database_closed_connection(DB_NAME)


def execute_get_request(request: str) -> list:
    global cur
    if cur is None:
        conn_cur_init()
    cur.execute(request)
    print_database_get_request_completed()
    return cur.fetchall()


def execute_set_request(request: str) -> None:
    global cur
    if cur is None:
        conn_cur_init()
    cur.execute(request)
    print_database_set_request_completed()
