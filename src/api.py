import sys
import json
import argparse

from parser import *
from storage import *
from utils import *

from flask import Flask, url_for, json, request

app = Flask(__name__)

@app.route("/add.json", methods = ['POST'])
def add():

    client_json = json.dumps(request.json)
    client_data = json.loads(client_json)
    returned_message = {}

    query_hostname = client_data['hostname']

    if hostname_resolves(query_hostname) == False:
        return "hostname did not resolve. exiting"

    # Lookups on the most common subdomains
    record_list = ['NS', 'MX', 'A', 'TXT', 'CNAME', 'AAAA']
    result = {}

    for record in record_list:
        result[record] = fetch_records(query_hostname, record)

    storage = Storage(query_hostname)

    # Let user know if details appear to have saved
    if storage.save(result):
        returned_message['message'] = 'success'
    else:
        returned_message['message'] = 'failure'

    return json.dumps(returned_message)


@app.route("/load.json", methods = ['POST'])
def load():
    client_json = json.dumps(request.json)
    client_data = json.loads(client_json)

    query_hostname = client_data['hostname']

    if hostname_resolves(query_hostname) == False:
        return "hostname did not resolve. exiting"

    storage = Storage(query_hostname)

    return storage.load()


def main():
    parser = argparse.ArgumentParser(description='Meta Reverse Image Search API')
    parser.add_argument('-p', '--port', type=int, default=5000, help='port number')
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    args = parser.parse_args()

    if args.debug:
        app.debug = True

    app.run(host='0.0.0.0', port=args.port)

if __name__ == '__main__':
    main()

