# QuantaStor
## OSNEXUS QuantaStor Python Client Library
---
### Storage Volume Example

One use case for the QuantaStor system is to allocate a storage volume to a host. As a requirement for the `example_sv.sh` script you should set up a storage pool called 'DefaultPool' using one or more storage device(s) using the CLI or GUI. This script also requires `sudo` privileges to use the `qs-util` tool-set. To run the example script use the following command-line code, from this directory replacing `x.x.x.x`, `username`, and `password` with the IP address of your QuantaStor server and your own credentials:

    $ source example_sv.sh x.x.x.x username password

Expected Result: From the GUI you should see that a storage volume was created named 'testVol'. From your terminal you should see your host ISCSI IQN printed out and a successful login message from the `qs-util iscsilogin` command. The terminal output should look something like this:

    Begging Quatastor Storage Volume setup example
    Created Storage Volume: 'testVol'
    Created Host: 'testHost'
    Attached ACL between 'testHost' & 'testVol'
    [sudo] password for user:
    iqn = iqn.xxxx-xx.org.debian:xx:xxxxxxxx
    logging host into ISCSI Block Storage
    INFO: iSCSI IQN: iqn.xxxx-xx.org.debian:xx:xxxxxxxxxxx
    x.x.x.x:3260,1 iqn.xxxx-xx.com.osnexus:xxxxxxxx-xxxxxxxxxxxx:testVol
    Logging in to [iface: default, target: iqn.xxxx-xx.com.osnexus:xxxxxxxx-xxxxxxxxxxxxxx:testVol, portal: x.x.x.x,3260] (multiple)
    Login to [iface: default, target: iqn.xxxx-xx.com.osnexus:xxxxxxxx-xxxxxxxxxxxxxx:testVol, portal: x.x.x.x,3260] successful.

To log out of the session use the following command:

    $ sudo iscsiadm -m session --logout