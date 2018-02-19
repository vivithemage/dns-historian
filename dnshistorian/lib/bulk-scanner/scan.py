from threading import Thread
from hostname import *

class BulkDNSScan():
    """
    The core aim of BulkDNSScan is to attempt to identify all the dns records a domain has.
    Essentially
    """
    def __init__(self):
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
            'lkjkui.'
        ];


    def run(self, domain):
        '''
        Lookups on the most common record types and returns a json object for processing
        This is done by checking if the
        '''

        result = {}
        hostname = Hostname()

        for subdomain in self.subdomain_list:
            for record_type in self.record_type_list:

                full_domain = subdomain + domain


                content_array = hostname.content(full_domain, record_type)

                if content_array is not False:
                    log_message = 'Found: ' + record_type + ' of ' + full_domain
                    print(log_message)
                    print(content_array)


            """if (content_array):
                for content in content_array:
                    print(content)
                    """

if __name__ == '__main__':
    scanner = BulkDNSScan()
    scanner.run('mage.me.uk')
