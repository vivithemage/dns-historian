import os
import sys
import json
import socket
import datetime

import dns.resolver
import dns.query
import dns.zone

from flask import Flask, url_for, json, request

query_domain = sys.argv[1]
log_root_directory = sys.argv[2]

def fetch_records(query_domain, record_type) :
    record_array = []

    try :
        for record in dns.resolver.query(query_domain, record_type) :
            record_array.append(str(record))

        return record_array

    except dns.resolver.NoAnswer:
        return ['no records']

# Create domain directory if it does not already exist and save with timestamp
def save(result):
    # Wrap up in json
    result_json = json.dumps(result, indent=4)
    log_file_timestamp = datetime.datetime.now().strftime("_%A_%d_%B_%Y_%I_%M%p")
    log_file_name = query_domain + log_file_timestamp + '.json'
    log_file_full_path = log_root_directory + '/' + query_domain + '/' + log_file_name

    log_directory = log_root_directory + '/' + query_domain

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = open(log_file_full_path, "w")
    log_file.write(result_json)
    log_file.close()


# Lookups on the most common subdomains
record_list = ['NS', 'MX', 'A', 'TXT', 'CNAME', 'AAAA']
result = {}

for record in record_list:
    result[record] = fetch_records(query_domain, record)

save(result)

## Scheduled check

# find the domain with the oldest lookup

# run the same scan as initial lookup

# If there is a difference, save it as a new file

# otherwise update the existing file with a timestamp
