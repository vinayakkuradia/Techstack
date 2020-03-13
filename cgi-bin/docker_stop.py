#!/usr/bin/python36
import subprocess
import cgi

print("content-type: text/html")


form = cgi.FieldStorage()

cname = form.getvalue("s")

cmd = "sudo docker stop {}".format(cname)

x = subprocess.getoutput(cmd)

print("location: /cgi-bin/run.py")
print()



