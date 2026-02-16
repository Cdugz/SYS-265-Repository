#secure-ssh.sh
#author Cdugz
#creates a new ssh user using $1 parameter
#adds a public key from the local repo or curled from the remote repo
#removes roots ability to ssh in

#!/bin/bash

useradd -m testuser

mkdir -p /home/testuser/.ssh
cp ../public-keys/id_rsa.pub /home/testuser/.ssh/authorized_keys
chmod 600 /home/testuser/.ssh/authorized_keys
chmod 700 /home/testuser/.ssh
chown -R testuser:testuser /home/testuser/.ssh


