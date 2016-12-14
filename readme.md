DNS Historian
-------------

DNS Historian takes a hostname, periodically looks up common record types (NS, MX, A, TXT, CNAME, AAAA) and record them as flatfiles in json format.

Add a domain (example.com) using:

		curl -X POST -H "Content-Type: application/json" -d '{"hostname":"example.com"}' http://localhost:5000/dns-historian


Retrieve a domain using:
		curl http://localhost:5000/dns-historian?hostname=example.com

Setup and run

		git clone ..
		pip install
		cd dns-historian
		python src/dns-historian.py

Need help
