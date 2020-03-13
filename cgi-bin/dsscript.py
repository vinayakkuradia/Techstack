#!/usr/bin/python36

import os
import getpass as gp

ip = str(input("Enter IP: "))
pswd = str(gp.getpass("Enter password: "))

os.system("sudo sshpass -p '"+pswd+"' scp /var/www/cgi-bin/caas.py "+ip+":/tmp/")
os.system("sudo sshpass -p '"+pswd+"' scp /lwsoft/jdk.rpm "+ip+":/tmp/")
os.system("sudo sshpass -p '"+pswd+"' scp /lwsoft/hadoop.rpm "+ip+":/tmp/")
os.system("sudo sshpass -p '"+pswd+"' ssh "+ip+" /tmp/caas.py")
