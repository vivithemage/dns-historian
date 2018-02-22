from threading import Thread
from collections import defaultdict
from hostname import *
import pprint

class BulkDNSScan():
    """
    The core aim of BulkDNSScan is to attempt to identify all the dns records a domain has.
    Essentially
    """
    def __init__(self):
        self.complete_results = defaultdict(list)

        self.record_type_list = ['NS', 'MX', 'A', 'TXT', 'CNAME', 'AAAA']

        """ 
        Most common subdomains taken from http://bit.ly/1U8ptjI 
        There is an empty one so the root domain is scanned too 
        """

        self.subdomain_list = [
            '',
            'www.',
            'mail.',
            'remote.',
            'blog.',
            'webmail.',
            'server.',
            'ns1.',
            'ns2.',
            'smtp.',
            'secure.',
            'vpn.',
            'm.',
            'shop.',
            'ftp.',
            'mail2.',
            'test.',
            'portal.',
            'ns.',
            'ww1.',
            'host.',
            'support.',
            'dev.',
            'web.',
            'bbs.',
            'ww42.',
            'mx.',
            'email.',
            'cloud.',
            'mail1.',
            'forum.',
            'owa.',
            'www2.',
            'gw.',
            'admin.',
            'store.',
            'mx1.',
            'cdn.',
            'api.',
            'exchange.',
            'app.',
            'gov.',
            '2tty.',
            'vps.',
            'govyty.',
            'hgfgdf.',
            'news.',
            '1rer.',
            'lkjkui.',
            'pop.',
            'smtp.',
            'backup'
        ];

    def scan_thread(self, subdomain, domain):
        hostname = Hostname()
        subdomain_results = defaultdict(list)

        for record_type in self.record_type_list:
            full_domain = subdomain + domain

            content_array = hostname.content(full_domain, record_type)
            subdomain_results[record_type].append(content_array)

        self.complete_results[subdomain].append(subdomain_results)


    def run(self, domain):
        '''
        Lookups on the most common record types and returns a json object for processing
        This is done by checking if the
        '''

        threads = []

        for subdomain in self.subdomain_list:
            # print("Starting thread: " + subdomain)
            thread = Thread(target=self.scan_thread, args=(subdomain, domain))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return self.complete_results


if __name__ == '__main__':
    scanner = BulkDNSScan()
    results = scanner.run('mage.me.uk')
    print("finished")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(results)

