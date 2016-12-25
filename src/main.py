import os
import sys
import json
import socket
import datetime
import argparse

import dns.resolver
import dns.query
import dns.zone

from flask import Flask, url_for, json, request

app = Flask(__name__)

def fetch_records(query_hostname, record_type) :
    record_array = []

    try :
        for record in dns.resolver.query(query_hostname, record_type) :
            record_array.append(str(record))

        return record_array

    except dns.resolver.NoAnswer:
        return ['no records']

# Create domain directory if it does not already exist and save with timestamp
def save(result, query_hostname):
    # Wrap up in json
    log_root_directory = 'logs'
    result_json = json.dumps(result, indent=4)
    log_file_timestamp = datetime.datetime.now().strftime("_%A_%d_%B_%Y_%I_%M%p")
    log_file_name = query_hostname + log_file_timestamp + '.json'
    log_file_full_path = log_root_directory + '/' + query_hostname + '/' + log_file_name

    log_directory = log_root_directory + '/' + query_hostname

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = open(log_file_full_path, "w")
    log_file.write(result_json)
    log_file.close()

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False


@app.route("/", methods = ['POST'])
def add():
    if request.headers['Content-Type'] != 'application/json':
        return "Requests must be in JSON format. Please make sure the header is 'application/json' and the JSON is valid."


    client_json = json.dumps(request.json)
    client_data = json.loads(client_json)

    query_hostname = client_data['hostname']

    if hostname_resolves(query_hostname) == False:
        return "hostname did not resolve. exiting"


    # Lookups on the most common subdomains
    record_list = ['NS', 'MX', 'A', 'TXT', 'CNAME', 'AAAA']
    result = {}

    for record in record_list:
        result[record] = fetch_records(query_hostname, record)

    save(result, query_hostname)

    return json.dumps(result, ensure_ascii=False)


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

## Scheduled check

# find the domain with the oldest lookup

# run the same scan as initial lookup

# If there is a difference, save it as a new file

# otherwise update the existing file with a timestamp
