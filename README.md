# DNS Historian


## V2

The whole system consists of three different sections.
The first is the scanner. This looks through the database and periodically does all the lookups on hostnames to see if they have changed and writes any new changes.
The second is the rest api. This essentially deals with all requests and sends back relevant info.
The last is the frontend which essentially (ionic - html, css, js)

## Scanner

This never interacts with the rest api. All it does is read the mongodb database.

Classes and overview of use

Scanner - Creates and calls all the different tasks
Storage
Hostname






## V1

DNS Historian takes a hostname, periodically looks up common record types (NS, MX, A, TXT, CNAME, AAAA) and records them as flatfiles in json format.

*Add a domain (example.com) using:*

	curl -X POST -H "Content-Type: application/json" -d '{"hostname":"example.com"}' http://localhost:5000/write.json

*Retrieve a domain using:*

	curl -X POST -H "Content-Type: application/json" -d '{"hostname":"example.com"}' http://localhost:5000/read.json

*Setup and run*

	pip install flask python-dnspython requests
	cd dns_historian
	python dns-historian.py

*Scheduled DNS lookups*

Once the hostname is added, it needs to be periodically checked for changes.  This is done with updater.py. A quick way to get started is simply install tmux and then:

	tmux
	python updater.py
