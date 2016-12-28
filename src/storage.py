import os
import sys
import json
import datetime

from utils import *

class Storage:

    def __init__(self, hostname):
        self.hostname = hostname
        self.log_directory = 'logs'

        # set flags on which storage system to use
        self.flat_system = True
        self.mongodb_system = False

    def db_connect():
        from pymongo import MongoClient

        self.mongodb_connection = 'localhost:27017'
        client = MongoClient(self.mongodb_connection)
        db = client.dnsHistorian

        return db

    def save_flat(self, result):
        timestamp_format = "_%y-%m-%dT%H-%M-%S"

        result_json = json.dumps(result, indent=4)
        log_file_timestamp = datetime.datetime.now().strftime(timestamp_format)
        log_file_name = self.hostname + log_file_timestamp + '.json'
        log_file_full_path = self.log_directory + '/' + self.hostname + '/' + log_file_name

        self.log_directory = self.log_directory + '/' + self.hostname

        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        try:
            log_file = open(log_file_full_path, "w")
            log_file.write(result_json)
        except IOError:
            return False
        else:
            log_file.close()
            return True


    def load_flat(self, limit):
        directory = self.log_directory + '/' + self.hostname
        files = sorted(os.listdir(directory))

        newest = files[0:limit]

        result = {}
        i = 0

        for file_name in reversed(newest):
            json_string = file_get_contents(directory + '/' + file_name)
            result[file_name] = json.loads(json_string)
            i = i + 1

        return json.dumps(result)

    def save_db(self, result):
        db = self.db_connect
        #db.dns_lookup.insert({"hostname" : self.hostname})
        #print json_data

    def save(self, result):
        if self.flat_system:
            return self.save_flat(result)

    def load(self, limit = 10):
        if self.flat_system:
            return self.load_flat(limit)


