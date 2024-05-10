import os
import sys


def main():
    try:
        os.environ['host'] = sys.argv[1]
        os.environ['port'] = sys.argv[2]
        print(os.getenv('host'))
    except IndexError:
        print('Usage: main.py <host> <port>')
        return


if __name__ == '__main__':
    main()