#!/usr/bin/python36

import os
import subprocess


def javacheck():
	ch1 = str(subprocess.getoutput("java -version"))
	if ("Java HotSpot" in ch1):
		hadoopcheck()
	
	else:
		#Java installation and Path setup code
		jdkstats = str(subprocess.getstatusoutput("rpm -i /tmp/jdk.rpm"))
		if jdkstats[1] == "0":
			os.system("echo \"\n\nexport JAVA_HOME=/usr/java/jdk1.8.0_171-amd64\nexport PATH=/usr/java/jdk1.8.0_171-amd64/bin:\$PATH\" | cat >> /root/.bashrc")
		hadoopcheck()

def hadoopcheck():
	ch2 = str(subprocess.getoutput("hadoop version"))
	if ("hadoop/hadoop-core" in ch2):
		nnconfig()
	else:
		#Hadoop installation code
		os.system("rpm -i /tmp/hadoop.rpm --force")
		nnconfig()

def nnconfig():
	#host-name
	os.system("hostnamectl set-hostname namenode.ts-client.com")	
	#hdfs-site.xml
	os.system("mkdir /master")
	os.system("sed -i 's+</configuration>++g' /etc/hadoop/hdfs-site.xml")
	os.system("sed -i 's+<configuration>+<configuration>\\n\\n<property>\\n<name>dfs.name.dir</name>\\n<value>/master</value>\\n</property>\\n\\n</configuration>+g' /etc/hadoop/hdfs-site.xml")
	#core-site.xml
	mip = str(subprocess.getoutput("ifconfig enp0s3 | grep netmask | awk '{print $2}'"))
	os.system("sed -i 's+</configuration>++g' /etc/hadoop/core-site.xml")
	os.system("sed -i 's+<configuration>+<configuration>\\n\\n<property>\\n<name>fs.default.name</name>\\n<value>hdfs://"+mip+":9001</value>\\n</property>\\n\\n</configuration>+g' /etc/hadoop/core-site.xml")
	#format master
	os.system("hadoop namenode format")
	os.system("iptables -F")
	os.system("hadoop-daemon.sh start namenode")
	os.system("rm -f /tmp/jdk.rpm")
	os.system("rm -f /tmp/hadoop.rpm")
	

#Initiation Point
javacheck()
