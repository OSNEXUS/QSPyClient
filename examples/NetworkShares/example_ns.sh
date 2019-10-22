#! /bin/bash

if [ $# -ne 3 ]; then
    echo "not the right amount of args"
    echo "usage: source example_ns.sh [hostIP] [username] [password]"
    return 1
fi

echo "Begging Quatastor Network Share setup example"

python3 shr_setup.py $1 $2 $3

echo "Created Network Share: 'testShare'"

if [ ! -d /mnt/testMount ]; then
    sudo mkdir /mnt/testMount
    echo "Created Directory: '/mnt/testMount'."
else
    echo "Dir: '/mnt/testMount' already exists."
fi

echo "Mounting share to '/mnt/testMount'." 

sudo mount $1:/export/testShare/ /mnt/testMount/

echo "Displaying active mount to 'testShare': "

mount | grep -i "testShare"
