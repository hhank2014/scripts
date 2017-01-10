#!/bin/bash

Server=$1
ProjectName=$2

ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no root@${Server} "if [ -d /data/www/${ProjectName}static ];then echo 'exist';else mkdir /data/www/${ProjectName}static -p;fi"
rsync -avz --delete --partial --exclude-from=/etc/rsync-exclude-php.list -e \
"ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no" src/${ProjectName}/ root@${Server}:/data/www/${ProjectName}static/${ProjectName} |grep -v /$
rsync -avz --delete --partial --exclude-from=/etc/rsync-exclude-php.list -e \
"ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no" src/common/ root@${Server}:/data/www/${ProjectName}static/common |grep -v /$
