from threading import Thread
from hostname import *
import pprint


class BulkDNSScan():
    """
    Bulk DNS Scanner attempts to identify all the key DNS records a domain has.
    """
    def __init__(self, record_types = None, subdomains = None):
        """
        If the user does not pass a list of record types,
        """
        if subdomains is not None:
            self.subdomain_list = subdomains
        else:
            self.subdomain_list = ['__root', 'www', 'mail'];

        if record_types is not None:
            self.record_type_list = record_types
        else:
            self.record_type_list = ['NS', 'MX', 'A', 'TXT', 'CNAME', 'AAAA']

        self.complete_results = dict.fromkeys(self.subdomain_list)

        for subdomain in self.subdomain_list:
            self.complete_results[subdomain] = dict.fromkeys(self.record_type_list)

    def _full_hostname(self, subdomain, domain):
        if subdomain is '__root':
            full_domain = domain
        else:
            full_domain = subdomain + '.' + domain

        return full_domain

    def _scan_thread(self, subdomain, domain, record_type):
        hostname = Hostname()
        full_hostname = self._full_hostname(subdomain, domain)
        content_array = hostname.content(full_hostname, record_type)

        if content_array is not False:
            self.complete_results[subdomain][record_type] = content_array

        """ print("adding " + subdomain  + " to " + record_type + " using " + str(content_array)) """

    def run(self, domain):
        '''
        Start a thread for each subdomain and record combination.
        All threads write directly do complete_results
        '''

        threads = []

        for subdomain in self.subdomain_list:
            for record_type in self.record_type_list:
                thread = Thread(target=self._scan_thread, args=(subdomain, domain, record_type))
                thread.start()
                threads.append(thread)
                
        for thread in threads:
            thread.join()

        return self.complete_results


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    scanner = BulkDNSScan()
    results = scanner.run('example.com')
    pp.pprint(results)


