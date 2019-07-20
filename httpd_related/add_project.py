import os

# get project dir name & url
project = raw_input("pleace input your project folder name in projects folder:")
url = raw_input("pleace input your custom local web url:")
is_laravel = raw_input('Is it laravel project?(Y or N): ')

if (is_laravel == 'Y'):
    project = project+'/public'

# add host url in local
fo = open("/etc/hosts", "a")
fo.write('\n')
fo.write("127.0.0.1 {}".format(url))
fo.close()
# add httpd-vhost project dir
vhosts = open("/usr/local/etc/httpd/extra/httpd-vhosts.conf", "a")
vhosts.write('\n')
vhosts.write('\n')
template = open("/Users/logic/useful_tools/template.txt", "r").read()
vhosts.write(template%(project,project,url))
vhosts.close()
# restart apache
os.system("/usr/local/bin/apachectl -k restart")
os.system("open -a 'Google Chrome' http://%s"%(url))