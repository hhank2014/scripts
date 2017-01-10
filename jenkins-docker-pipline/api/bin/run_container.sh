#!/bin/bash
#by huangjie

ProjectName=$1
Release=$2
RegistryIP="192.168.221.134"
RegistryPORT="5000"
RegistryPro="tomtop"
Locallogs="/data/logs/${ProjectName}"
APILogs="/usr/local/tomcat-${ProjectName}/logs"
Date=`date +"%m%d%H%M"`
DockerName=${ProjectName}${Date}

if [ -d ${Locallogs} ]
then
	echo "exist"
else
	mkdir ${Locallogs}
fi

Cid=`docker ps | grep ${ProjectName} | awk '{print $1}'`

RegistryURL="${RegistryIP}:${RegistryPORT}/${RegistryPro}/${ProjectName}:${Release}"

docker pull ${RegistryURL}

if [ ${Cid} ];then
        docker run -d --name ${DockerName} -P -v ${Locallogs}:${APILogs} -v /etc/hosts:/etc/hosts ${RegistryURL}
        docker stop ${Cid}
else
        docker run -d --name ${DockerName} -P -v ${Locallogs}:${APILogs} -v /etc/hosts:/etc/hosts ${RegistryURL}
fi
