#!/usr/bin/python36
import subprocess
import cgi

print("content-type: text/html")
print()

ctr = cgi.FieldStorage()
name = ctr.getvalue('n')

x = str(subprocess.getoutput("sudo useradd {}".format(name)))
if x[1] == "0":
	print("The user was created successfully!")
else:
	print("Username not available or some error occured.")

print("<meta http-equiv = \"refresh\" content = \"3; url = /TechStack/index.html\" />")
