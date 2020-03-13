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
	os.system("rm -f /tmp/jdk.rpm")
	os.system("rm -f /tmp/hadoop.rpm")
	

#Initiation Point
javacheck()
