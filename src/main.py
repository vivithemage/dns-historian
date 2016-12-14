import socket
import dns.resolver
import dns.query
import dns.zone

## Initial add of hostname

query_domain = 'google.co.uk'

# Get the nameservers of the domain

def fetch_records(query_domain, record_type) :
    record_array = []

    try :
        for record in dns.resolver.query(query_domain, record_type) :
            record_array.append(record)

        return record_array

    except dns.resolver.NoAnswer:
        return ['no records']

record_list = ['NS', 'MX', 'A', 'TXT', 'CNAME', 'AAAA']
result = {}

for record in record_list:
    result[record] = fetch_records(query_domain, record)
    print record + " >> "
    print result[record]

# Try and do a zone transfer
#z = dns.zone.from_xfr(dns.query.xfr('204.152.189.147', 'dnspython.org'))
#names = z.nodes.keys()
#names.sort()
#for n in names:
#    print z[n].to_text(n)

# if a zone transfer is not supported, do lookups on the most common subdomains

# Wrap up in json file

# Create domain directory if it does not already exist and save with timestamp



## Scheduled check

# find the domain with the oldest lookup

# run the same scan as initial lookup

# If there is a difference, save it as a new file

# otherwise update the existing file with a timestamp
