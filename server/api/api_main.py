import re

from server.api.api_lib import lib


def make_response(request: str) -> str:
    for req in lib:
        if re.search(req, request) is not None:
            m = re.search(req, request)
            params = []
            i = 1
            while True:
                try:
                    params.append(m.group(i))
                    i += 1
                except IndexError:
                    break
            try:
                result = lib[req](*params)
                if result is not None:
                    return result+"\n"
                else:
                    return succeeded()
            except TypeError:
                return invalid_request()

    return invalid_request()


def invalid_request() -> str:
    return "Bad request.\n"

def succeeded() -> str:
    return "Succeeded.\n"
