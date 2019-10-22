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
    parser.add_argument("host", help="IP address of target QuantaStor server.")
    parser.add_argument("username", help="Username credentials.")
    parser.add_argument("password", help="Password credentials.")
    parser.add_argument("-c","--cert", help="Full path to SSL certificate.")
    args = parser.parse_args()

    if not args.cert:
        args.cert = ""

    if not quantastor_sdk_enabled():
        print('QuantaStor python SDK is required for this module.')

    client = QuantastorClient(args.host,args.username,args.password,args.cert)

    #create a storage volume
    try:
        task, obj, objlist = client.storage_volume_create_ex(name='testVol',provisionableId='DefaultPool',size="5G")
    except Exception as e:
        print ("EXCEPTION CAUGHT: " + str(e))

    #create a host
    try:
        task, obj = client.host_add(hostname='testHost')
    except Exception as e:
        print ("EXCEPTION CAUGHT: " + str(e))

    #attach acl to volume
    try:
        task, objlist = client.storage_volume_acl_add_remove_ex(storageVolumeList='testVol',host='testHost',modType=0)
    except Exception as e:
        print ("EXCEPTION CAUGHT: " + str(e))

main()
