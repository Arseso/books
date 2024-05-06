import secrets
import string
from server.core.logs import print_server_changed_role_for_user, \
    print_server_delete_user

from server.data import requests_library as lib
from server.data.requests import execute_get_request as db_get
from server.data.requests import execute_set_request as db_set
from server.data.usr import register, is_admin


def get_token(nick: str, passwd: str) -> str:
    data = db_get(request=lib.GET_USER_TOKEN.format(nick=nick, passwd=passwd))
    return data[0][0] if len(data) == 1 else register(nick=nick, passwd=passwd)


def set_admin(token_subject: str, token_object: str) -> str:
    if is_admin(token_subject):
        db_set(lib.SET_USER_ROLE.format(token=token_object, role="adm"))
        print_server_changed_role_for_user(token_subject, token_object)
    else:
        return "You must be an adm to changing role."


def del_user(token_subject: str, token_object: str):
    data = db_get(request=lib.GET_USER_ROLE.format(token=token_subject))
    if data[0][0] == "adm":
        db_set(lib.DEL_USER.format(token=token_object))
        print_server_delete_user(token_subject, token_object)
    else:
        return "You must be an adm to changing role."


def get_id_by_token(token: str) -> int:
    data = db_get(request=lib.GET_USER_ID.format(token=token))
    if len(data) == 0:
        return -1
    else:
        return int(data[0][0])


assert get_id_by_token(token="gy0so") == 4
assert get_id_by_token(token="sss") == -1
