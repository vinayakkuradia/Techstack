# Techstack
A responsive web interface to make latest technologies easily available to even non-technical people.

TechStack - AdHockers
=========================================================================
Setting up the CGI Project:-
1.Extract the given zip file
2.Replace both folders with the original ones or copy inside content without any changes,
	-"cgi-bin" with /var/www/cgi-bin
	-"html" with /var/www/html
Note:: "TechStack" folder must be inside "html" folder to make css fully work.
3.Run httpd/apache web server service. Open browser and enter http://~IP Addr~/TechStack
Note:: The transfer of setup files may take longer than usual especially in case of hadoop. So to avoid Server Timeout(Error 504) make an entry in /etc/httpd/conf/httpd.conf as described. Enter "TimeOut 600" just below (in next line) "Listen 80" and restart/start web server's service
=========================================================================
Guide to use this project:-
1.Index page brings you to a secondary/sub choice page on clicking "Launch".
2.The working project options are limitited as it's not fully developed. So particular options will work correctly for you. Correct sub-page option approach is provided below:
	-To Use Docker: Use "Run Server" option: This will execute "run.py" present in cgi-bin
	-To Use Hadoop: Use "Express" option, and enter IP and Password of target VM/PC, you want to cofigure as namenode: This will execute "tssrun.py" present in cgi-bin which will transfer required files and script to target VM/PC and will also further execute the sent script there and it will also remove setup files from target VM.
	-To Use HTTPD: Use "Express" option, and enter IP and Password of target VM/PC into which you want to install and configure HTTPD Web Server: This will execute "tssrun.py" present in cgi-bin which will transfer required script to target VM/PC and will also further execute the sent script there and it will also remove setup files from target VM.
==========================================================================
Suggested Further Development Ways:
---There are separate scripts for docker, while hadoop and htttpd use a general script namely "tssrun.py" to get their respective scripts and/or files transferred and run on target VMs/PCs---
1.Docker scripts currently monitor the containers of Web Server VM/PC. You will need to execute these scripts on another IP of VM/PC given by user and accordingly configure the command scripts namely docker_start.py, docker_stop.py and docker_terminate.py.
2.Hadoop's express option currently configure the target VM/PC as a namenode only. You will need to configure/copy the nnconfig.py as dnconfig.py(for example) and change current commands accordingly to configure VM as a datanode.
3.Currently HTTPD configurations are done as per default. But I wanted to make script which configure custom port and custom web directory too. For this, you can add custom port and custom directory commands in current httpd.py script. To do that, you will need to provide port no. and directory name through editing the httpd.py(automatically via code, via tssrun.py file) before transfering to target VM/PC. Don't forget to revert the changes made in cgi-bin httpd.py file to get used next time.
4.To make changes in WebUI, you'll need little/basic knowledge of HTML and/or JavaScript and/or JQuery. Still to simplify your work I'm telling you the simple way,
	-The "Express" button launches a "Modal" asking for IP and password, you can edit these details or options in sub-page.html(ex hadoop.html) file's upper part by looking/finding the same.
	-To run different script through that button you have to provide path for target script also, you can look the syntax in the written code.
	-To add an extra modal you can copy already present modal code and modify accordingly. But to activate that modal you have to edit javascript present in it's folder and assign an ID to button and it's target modal (in html file) so that you can use that ID in JQuery syntax.

THANK YOU!!!
=========================================================================
For any queries, Call +91-8239540487 or Email vkuradia87@gmail.com.
								-Vinayak Kuradia
