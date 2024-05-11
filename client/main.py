import os
import sys

import client.requests.req
from client.core.event_loop import init_event_loop, requests_queue


def main():
    requests_queue.append(client.requests.req.get_token("admin", "12345"))
    init_event_loop()


if __name__ == '__main__':
    main()
