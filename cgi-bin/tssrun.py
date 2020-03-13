#!/usr/bin/python36

import os
import cgi

var = cgi.FieldStorage()
ip = var.getvalue("ip")
pswd = var.getvalue("pswd")
script = var.getvalue("script")

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
    
    <title>Processing Client System...</title>

</head>

""")

os.system("sudo sshpass -p '"+pswd+"' scp /var/www/cgi-bin/"+script+".py "+ip+":/tmp/")
print("""<body class="default">
""")
if script == "nnconfig":
	os.system("sudo sshpass -p '"+pswd+"' scp /lwsoft/jdk.rpm "+ip+":/tmp/")
	os.system("sudo sshpass -p '"+pswd+"' scp /lwsoft/hadoop.rpm "+ip+":/tmp/")
os.system("sudo sshpass -p '"+pswd+"' ssh "+ip+" /tmp/"+script+".py")
print("""
   <h3 style="font-family: Sans-Serif">Operation completed successfully! Now redirecting to source page...</h3>
</body>
</html>
""")
print("<meta http-equiv = \"refresh\" content = \"5; url = /TechStack/hadoop.html\" />")
