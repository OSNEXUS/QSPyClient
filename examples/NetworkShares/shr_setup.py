# This is an example file for using the Quantastor Python Client (qs_client.py).
# for a simple demo:
# > create a symbolic link to qs_client.py in the python3.x dist-packages directory
# cmd: sudo ln -s  /full/path/to/qs_client.py /usr/local/lib/python3.6/dist-packages/qs_client.py
# > once the symlink has been created, you can run this program using the following command:
# cmd: python3 example.py [host IP]
# RESULTS: if the host IP exists

from quantastor.qs_client import QuantastorClient
from quantastor.qs_client import quantastor_sdk_enabled
from quantastor.qs_client import StorageSystem
import requests
import json
import sys
import argparse
from requests.auth import HTTPBasicAuth

def main():
    parser = argparse.ArgumentParser()
    # Required arguements
    parser.add_argument("host", help="IP address of target QuantaStor server.")
    parser.add_argument("username", help="Username credentials.")
    parser.add_argument("password", help="Password credentials.")
    # Optional arguements
    parser.add_argument("-c","--cert", help="Full path to SSL certificate.")
    args = parser.parse_args()

    if not args.cert:
        args.cert = ""

    # verify quantastor sdk
    if not quantastor_sdk_enabled():
        print('QuantaStor python SDK is required for this program.')

    # initiallize client
    client = QuantastorClient(args.host,args.username,args.password,args.cert)

    #create a network share
    try:
        task, obj = client.network_share_create_ex(name='testShare',provisionableId='DefaultPool',isActive=True,isPublic=True)
    except Exception as e:
        print ("Exception --> " + str(e))

main()
