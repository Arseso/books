import secrets
import string

from server.core.logs import print_server_new_user_registered

from server.data.requests import execute_set_request as db_set
from server.data.requests import execute_get_request as db_get
from server.data import requests_library as lib


def generate_token() -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(5))


def register(nick: str, passwd: str) -> str:
    token = generate_token()
    db_set(request=lib.SET_NEW_USER.format(nick=nick, passwd=passwd, token=token))
    print_server_new_user_registered(nickname=nick)
    return token


def is_admin(token: str) -> bool:
    role = db_get(request=lib.GET_USER_ROLE.format(token=token))
    if role[0][0] == 'adm':
        return True
    return False