import dns.resolver
import dns.query
import dns.zone

class Hostname():
    """
    Takes a hostname along with a record type and pulls through the content.
    """

    def get_record(self, query_hostname, record_type):
            try:
                resolver = dns.resolver.Resolver()
                """ Can these nameservers be randomized in order to prevent throttling? """
                resolver.nameservers = ['91.239.100.100']

                record = resolver.query(query_hostname, record_type)

            except:
                #print("Unexpected error:", sys.exc_info()[0])
                return False


            return record.response.answer[0].items

    def content(self, query_hostname, record_type):
        record_content = self.get_record(query_hostname, record_type)

        return record_content
