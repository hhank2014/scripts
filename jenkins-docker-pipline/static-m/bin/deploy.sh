#!/bin/bash

Server=$1
ProjectName=$2
staticdir="/data/www/${ProjectName}static"
Project="m${ProjectName}"
common="mcommon"

ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no root@${Server} "if [ -d ${staticdir} ];then echo 'exist';else mkdir ${staticdir} -p;fi"
rsync -avz --delete --partial --exclude-from=/etc/rsync-exclude-php.list -e \
"ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no" src/${Project}/ root@${Server}:${staticdir}/${Project} |grep -v /$
rsync -avz --delete --partial --exclude-from=/etc/rsync-exclude-php.list -e \
"ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no" src/${common}/ root@${Server}:${staticdir}/${common} |grep -v /$
