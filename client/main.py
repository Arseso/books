import os
import sys

import client.requests.req
from client.core.event_loop import init_event_loop
from client.ui.auth import init_auth


def main():
    init_event_loop()
    init_auth()

if __name__ == '__main__':
    main()
