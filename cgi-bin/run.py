#!/usr/bin/python36

import subprocess

print("content-type: text/html")
print()

print("""
<!DOCTYPE html>
<html lang="en">

<head>

    <!-- Required meta tags always come first -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">

    <!-- Bootstrap CSS -->
    <!-- build:css css/main.css -->
    <link rel="stylesheet" href="/TechStack/node_modules/bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/TechStack/node_modules/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="/TechStack/node_modules/bootstrap-social/bootstrap-social.css">
    <link rel="stylesheet" href="/TechStack/fonts/style.css">
    <link rel="stylesheet" type="text/css" href="/TechStack/css/styles.css">
    <!-- endbuild -->
    
    <title>Tech-Stack: Docker Engine</title>

</head>

""")

output = subprocess.getoutput("sudo docker ps -a")


container_list = output.split("\n")

print("""
<body class="default">
<iframe width='100%' name='myconsole'></iframe>""")

print("""
<table class="table dockertab" width='100%'>
<tr>
<th>Container Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>""")

for c  in container_list[1:]:
	if "Up" in c:
		cstatus = "running"
	elif  "Exited" in c:
		cstatus = "stopped"
	else:
		status = "unknown status"
	c_details  =  c.split()
	cname =  c_details[-1]
	imagename = c_details[1]

	print('''

	<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='/cgi-bin/docker_start.py?s={}'>Start</a></td>
	<td><a href='/docker_stop.py?s={}'>Stop</a></td>
	<td><a href='/docker_terminate.py?s={}'>Terminate</a></td>
	<td><a target='myconsole' href='http://192.168.1.97:4200'>Console</a></td>
	</tr>
	'''.format(cname, imagename, cstatus, cname, cname, cname, cname ))



print("</table>")
print("</body>")
print("</html>")

