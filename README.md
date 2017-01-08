DNS Historian
-------------

DNS Historian takes a hostname, periodically looks up common record types (NS, MX, A, TXT, CNAME, AAAA) and record them as flatfiles in json format.

*Add a domain (example.com) using:*

	curl -X POST -H "Content-Type: application/json" -d '{"hostname":"example.com"}' http://localhost:5000/write.json

*Retrieve a domain using:*

	curl -X POST -H "Content-Type: application/json" -d '{"hostname":"example.com"}' http://localhost:5000/read.json

*Setup and run*

	pip install flask python-dnspython requests
	git clone
	cd dns-historian/dns-historian
	python dns-historian.py

*Scheduled DNS lookups*

Once the hostname is added, it needs to be periodically checked for changes.  This is done with updater.py. A quick way to get started is simply install tmux and then:

	tmux;
	python updater.py;
