import sys
import json
import argparse

from parser import *
from storage import *
from utils import *

from flask import Flask, url_for, json, request

app = Flask(__name__)

@app.route("/write.json", methods = ['POST'])
def write():
    client_json = json.dumps(request.json)
    client_data = json.loads(client_json)
    returned_message = {}
    query_hostname = client_data['hostname']

    if hostname_resolves(query_hostname) is not True:
        returned_message['message'] = 'failure - hostname did not resolve'
        return json.dumps(returned_message)

    # Lookups on the most common record types
    record_list = ['NS', 'MX', 'A', 'TXT', 'CNAME', 'AAAA']
    result = {}

    for record in record_list:
        result[record] = get_records(query_hostname, record)

    storage = Storage(query_hostname)

    # Let user know if details appear to have saved
    returned_message['message'] = 'failure - could not save result'

    if storage.save(result):
        returned_message['message'] = 'success'

    return json.dumps(returned_message)


@app.route("/read.json", methods = ['POST'])
def read():
    client_json = json.dumps(request.json)
    client_data = json.loads(client_json)

    query_hostname = client_data['hostname']

    if hostname_resolves(query_hostname) is not True:
        returned_message['message'] = 'failure - hostname did not resolve'
        return json.dumps(returned_message)

    storage = Storage(query_hostname)

    return storage.load()


def main():
    parser = argparse.ArgumentParser(description='DNS Historian')
    parser.add_argument('-p', '--port', type=int, default=5000, help='port number')
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    args = parser.parse_args()

    if args.debug:
        app.debug = True

    app.run(host='0.0.0.0', port=args.port)

if __name__ == '__main__':
    main()

