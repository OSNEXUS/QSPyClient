# This is an example file for using the Quantastor Python Client (qs_client.py).
# for a simple demo:
# > create a symbolic link to qs_client.py in the python3.x dist-packages directory
# cmd: sudo ln -s  /full/path/to/qs_client.py /usr/local/lib/python3.6/dist-packages/qs_client.py
# > once the symlink has been created, you can run this program using the following command:
# cmd: python3 example.py [host IP]
# RESULTS: if the host IP exists 

from qs_client import QuantastorClient
from qs_client import quantastor_sdk_enabled
from qs_client import StorageSystem
import requests
import json
import sys
import argparse
from requests.auth import HTTPBasicAuth

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="IP address of target QuantaStor server.")
    parser.add_argument("username", help="Username credentials.")
    parser.add_argument("password", help="Password credentials.")
    parser.add_argument("-c","--cert", help="Full path to SSL certificate.")
    args = parser.parse_args()

    if not args.cert:
        args.cert = ""

    if not quantastor_sdk_enabled():
        print('QuantaStor python SDK is required for this program.')

    client = QuantastorClient(args.host,args.username,args.password,args.cert)

    try:
        system = client.storage_system_get()
        print (json.dumps(system.exportJson(), sort_keys=True,  indent=4, separators=(',', ': ')))
        
    except Exception as e:
        print ("Exception --> " + str(e))

main()
