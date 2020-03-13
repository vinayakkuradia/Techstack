#!/usr/bin/python36

import os
import subprocess


x = str(subprocess.getstatusoutput("yum install httpd -y"))
if x[1] == "0":
	subprocess.getoutput("echo 'This is a test page!' > /var/www/html/index.html")
	subprocess.getstatusoutput("systemctl stop firewalld")
	subprocess.getstatusoutput("systemctl disable firewalld")
	y = str(subprocess.getstatusoutput("systemctl restart httpd"))
	subprocess.getstatusoutput("systemctl enable httpd")


print("content-type: text/html")
print()


print("""
<html>
<head>
<link rel="stylesheet" href="fonts/style.css">
<title>Redirecting...</title>
</head>
<body style=\"background-color=#0A191E; color:aliceblue; font-family:'Brandon Grotesque Light'\">
<h2>Operation completed successfully! Now redirecting to source page...</h2>
</body>
</html>
""")
print("<meta http-equiv = \"refresh\" content = \"5; url = /TechStack/httpd.html\" />")
