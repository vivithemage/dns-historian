import os
import json
import datetime

from dnshistorian._utils import *


class Storage:

    def __init__(self, hostname):
        self.hostname = hostname
        self.log_directory = 'logs/' + hostname
        self.limit = 10

        # set flags on which storage system to use
        self.flat_system = True

    def list_files(self):
        files = sorted(os.listdir(self.log_directory))

        file_list = files[0:self.limit]

        return file_list

    def get_records(self):
        files = self.list_files()

        result = {}
        i = 0

        for file_name in reversed(files):
            json_string = file_get_contents(self.log_directory + '/' + file_name)
            result[file_name] = json.loads(json_string)
            i = i + 1

        return result

    def get_newest_filename(self):
        files = self.list_files()

        if files:
            return files[-1]
        else:
            return False

    # TODO
    def dns_changed(self, result):
        newest_filename = self.get_newest_filename()

        # DNS has changes as we have no record if it
        if newest_filename is False:
            return True

        newest_json_string = file_get_contents(self.log_directory + '/' + newest_filename)

        # Set both to json so a comparison can be made
        sent = result
        sent_json =  json.dumps(sent)

        newest = json.loads(newest_json_string)
        newest_json = json.dumps(newest)

        if newest_json == sent_json:
            return False
        else:
            return True

    def save_flat(self, result):

        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        result_json = json.dumps(result, indent=4)

        # If exactly the same, nothing to do
        if self.dns_changed(result) is False:
            return True

        timestamp_format = "_%y-%m-%dT%H-%M-%S"
        log_file_timestamp = datetime.datetime.now().strftime(timestamp_format)
        log_file_name = self.hostname + log_file_timestamp + '.json'
        log_file_full_path = self.log_directory + '/' + log_file_name

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

