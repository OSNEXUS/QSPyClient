# QuantaStor
## OSNEXUS QuantaStor Python Client Library

---

The python library for QuantaStor simplifies the process of automating QuantaStor management operations via python scripts.  All of the published QuantaStor REST APIs as documented on the OSNEXUS documentation [wiki](https://wiki.osnexus.com/index.php?title=REST_API_Reference_Guide) are callable via the python client.

---
## System Requirements for QuantaStor

The QuantaStor Python Client Library requires a QuantaStor box to interact with. The minimum requirements for your storage system vary based on the workload. Use our [Solution Design Tools](https://www.osnexus.com/design) to help you find the solution that best fits your use-case and budget. The minimum requirements provided in this documentation serves as the bare minimum to explore using the software and its capabilities.

* Intel Xeon or AMD x64 bit server (or virtual server) 
* 16GB RAM 
* 2x SSDs for system/boot drives
    - Boot drives should be hardware mirrored and should be atleast 64GB in size.
* One or more disks per system for storage pools. (SSD/NVMe/PCI SSD/SATA/SAS/FC/iSCSI/AoE)
* Download [QuantaStor USB/ISO Installation Media](https://www.osnexus.com/downloads) for installation.
---
## Installation

### Install Quantastor

To use the QuantaStor Python Client Library, you must first install QuantaStor on your server hardware or use a QuantaStor virtual system. Installation of QuantaStor will also include python3. QuantaStor ISO files are created as hybrid ISO files which can be written to DVD media with DVD writting software or directly copied to a USB flash drive using `dd`. Follow the [installation guide](https://wiki.osnexus.com/index.php?title=%2B_Installation_Guide_Overview) on our support wiki to get started. The installation guide provides instructions for installation and configuration on both server hardware and virtual machines.

### Run `pip` Installer

Using the PYPI pip installer run the following command to install the quantastor python client library:

On Linux/Unix

    $ sudo python3 -m pip install quantastor-pkg

### Testing qs_client Installation

Start the python3 interpreter:

    $ python3

Import `quantastor_sdk_enabled()` function from the library:

    >>> from quantastor.qs_client import quantastor_sdk_enabled

The following should print out 'True':

    >>> print (quantastor_sdk_enabled())

---
## Examples

See the `./examples/` directory for examples:

1. **Basic Example**

The basic example for the QuantaStor Python Client Library (`example.py`) does one operation to get information about the storage system that is specified from the command line and dumps the response data in JSON format. You can use this Python script as a basic template to build off of for QuantaStor automation.

2. **StorageVolume**

The file `example_sv.sh` is a bash script that utilizes two python scripts, `vol_setup.py` and `acl_attach.py`, to create an example storage volume and host. It then utilizes the `qs-util` QuantaStor tool-set to add a host initiator and login to an ISCSI session with the example storage volume.

3. **NetworkShare**

The file `example_ns.sh` is a bash script that utilizes the `shr_setup.py` python script to create an example network share. Then using the zfs `mount` command, mounts the network share to the local mount directory `/mnt/testMount`.

---
## Python Interpreter Usage

To quickly do operations from the commandline you can easily utilize the QuantaStor Python Client Library strait from the Python3 interpreter. Run the following commands in the python interpreter to set up a client connection to your QuantaStor server. Replace 'hostIP', 'username', and 'password' with your own credentials:

    >>> from qs_client import QuantastorClient
    >>> client = QuantastorClient('hostIP', 'username', 'password')

Requests are sent using HTTPS see the 'SSL Certs' section to learn to generate your own 'qs-ca-cert' to use for host verification. If you do not provide your own ca-cert, your client will warn you that 'requests cannot be verified'.

Once you have generated an instance of the 'QuantastorClient' class you can start making REST service calls to your QuantaStor server. The following is a simple example usage similar to the 'example.py' script:

    >>> system = client.storage_system_get()

This command will return your QuantaStor storage system as a 'StorageSystem' object. You can view the meta of any object class in JSON format (pretty print) by using the StorageSystem.exportJson() function and the dumps() function from the python json module.

    >>> import json
    >>> print (json.dumps(system.exportJson(), sort_keys=True,  indent=4, separators=(',', ': ')))

For more information about our REST API methods and objects see our [Reference Guide](https://wiki.osnexus.com/index.php?title=REST_API_Reference_Guide).

---
## SSL Certs

The 'QuantastorClient' class supports HTTPS ca-cert verification. You can provide the full path to your certification file as the fourth argument when creating an instance of the 'QuantastorClient' class:

    client = QuantastorClient('hostIP', 'username', 'password','/full/path/to/cert')

The certification path is an optional argument, but you will be warned that your requests cannot be verified if you do not provide one or if your certification path does not exist. If you do provide a valid ca-cert file, REST service calls will only succeed if your SSL verification succeeds.