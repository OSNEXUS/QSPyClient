# QuantaStor
## OSNEXUS QuantaStor Python Client Library
---
### Network Share Example

One use case for the QuantaStor system is to allocate a Network Share and to mount it to a file system. As a requirement for the `example_ns.sh` script you should set up a storage pool called 'DefaultPool' using one or more storage device(s) using the CLI or GUI.  This script also requires `sudo` privileges to make a directory and mount the network share to it. To run the example script use the following command-line code, from this directory replacing `x.x.x.x`,`username`, and `password` with the IP address of your QuantaStor server and your own credentials:

    $ source example_sv.sh x.x.x.x username password

Expected Result: From the GUI you should see that a network share was created named 'testShare'. From your terminal you should see your mounted file system printed out from the zfs `mount` command. The terminal output should look something like this:

    Begging Quatastor Network Share setup example
    Created Network Share: 'testShare'
    Dir: '/mnt/testMount' already exists.
    Mounting share to '/mnt/testMount'.
    Displaying active mount to 'testShare': 
    x.x.x.x:/export/testShare on /mnt/testMount type nfs4 (rw,relatime,vers=4.2,rsize=524288,wsize=524288,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=x.x.x.x,local_lock=none,addr=x.x.x.x)

to unmount the network share use the following command:

    $ sudo umount /mnt/testMount

