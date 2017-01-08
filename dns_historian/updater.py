import os
import json
import time
import requests

while True:
    files = sorted(os.listdir('logs'))

    for hostname in files:
        time.sleep(1)
        try:
            url = "http://127.0.0.1:5000/write.json"
            values = {"hostname": hostname}
            r = requests.post(url, json = values)

            print ("updating: " + hostname)
            print ("response: " + r.text)
        except:
            print ("post request failed, skipping...")

    print ("Retrieving fresh directory listing and starting update again...")
