#!/bin/bash
ProjectName=$1
www="${ProjectName}m"
Release=$2
RegistryIP="192.168.221.134"
RegistryPORT="5000"
RegistryPro="tomtop"
VLogs="/data/logs/${www}"
Hosts="/etc/hosts"
Date=`date +"%m%d%H%M"`
DockerName=${www}${Date}
RegistryURL="${RegistryIP}:${RegistryPORT}/${RegistryPro}/${www}:${Release}"

Cid=`docker ps | grep ${www} | awk '{print $1}'`

docker pull ${RegistryURL}

if [ -d ${VLogs} ];then
        echo "exists"
else
        mkdir ${VLogs}
fi

if [ ${Cid} ];then
        docker run -d --name ${DockerName} -P -v ${VLogs}:${VLogs} -v ${Hosts}:${Hosts} ${RegistryURL}
        docker stop ${Cid}
else
        docker run -d --name ${DockerName} -P -v ${VLogs}:${VLogs} -v ${Hosts}:${Hosts} ${RegistryURL}
fi
