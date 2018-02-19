import socket, json
import dns.resolver
import dns.query
import dns.zone


class Hostname():
    """
    Takes a hostname along with a record type and pulls through the content.
    """

    def get_record(self, query_hostname, record_type):
            try:
                record = dns.resolver.query(query_hostname, record_type)

            except dns.resolver.NoAnswer:
                return False

            return record.response.answer[0].items

    def resolves(self, query_hostname):
        try:
            socket.gethostbyname(query_hostname)
            return True
        except socket.error:
            return False

    def content(self, query_hostname, record_type):

        if self.resolves(query_hostname) is not True:
            return False

        record_content = self.get_record(query_hostname, record_type)

        return record_content
