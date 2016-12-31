import os
import sys
import json
import datetime

from utils import *

class Storage:

    def __init__(self, hostname):
        self.hostname = hostname
        self.log_directory = 'logs'
        self.limit = 10

        # set flags on which storage system to use
        self.flat_system = True

    def get_log_directory(self):
        return self.log_directory + '/' + self.hostname

    def list_files(self):
        directory = self.get_log_directory()
        files = sorted(os.listdir(directory))

        file_list = files[0:self.limit]

        return file_list

    def get_records(self):
        directory = self.get_log_directory()
        files = self.list_files()

        result = {}
        i = 0

        for file_name in reversed(files):
            json_string = file_get_contents(directory + '/' + file_name)
            result[file_name] = json.loads(json_string)
            i = i + 1

        return result

    # TODO
    def dns_changed(self, result):
        stored_records = self.get_records()
        return False

    def save_flat(self, result):

        result_json = json.dumps(result, indent=4)

        # If exactly the same, nothing to do
        if self.dns_changed(result) is not False:
            return True

        timestamp_format = "_%y-%m-%dT%H-%M-%S"
        log_file_timestamp = datetime.datetime.now().strftime(timestamp_format)
        log_file_name = self.hostname + log_file_timestamp + '.json'
        log_file_full_path = self.log_directory + '/' + self.hostname + '/' + log_file_name

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

    def load_flat(self):
        result = self.get_records()

        return json.dumps(result)

    def save(self, result):
        if self.flat_system:
            return self.save_flat(result)

    def load(self):

        if self.flat_system:
            return self.load_flat()

