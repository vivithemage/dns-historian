import argparse

from dnshistorian._parser import *
from dnshistorian._storage import *
from dnshistorian._utils import *

from hostname import *

def run():
    hostname = Hostname()
    content_array = hostname.content('bbc.co.uk', 'aaaa')

    if (content_array):
        for content in content_array:
            print(content)


    """
    parser = argparse.ArgumentParser(description='DNS Historian')
    parser.add_argument('-p', '--port', type=int, default=5000, help='port number')
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    args = parser.parse_args()
    """


if __name__ == '__main__':
    run()

