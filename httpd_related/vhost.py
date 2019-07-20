import os;
# open or close vhost feature
# Include /usr/local/etc/httpd/extra/httpd-vhosts.conf


httpd = open("/usr/local/etc/httpd/httpd.conf", "r")
filedata = httpd.read()
status = filedata.find("#Include /usr/local/etc/httpd/extra/httpd-vhosts.conf")
if (status == -1):
    print('Vhost status: True')
else:
    print('Vhost status: False')

question = raw_input('Do you want to open or close vhost feature? (True=T, False=F): ')

if (str(question) == 'T'):
    filedata = filedata.replace('#Include /usr/local/etc/httpd/extra/httpd-vhosts.conf','Include /usr/local/etc/httpd/extra/httpd-vhosts.conf')
    message = 'Open Vhost'
else:
    filedata= filedata.replace('Include /usr/local/etc/httpd/extra/httpd-vhosts.conf','#Include /usr/local/etc/httpd/extra/httpd-vhosts.conf')
    message = 'Close Vhost'

# print(filedata)
httpd.close()

httpd = open("/usr/local/etc/httpd/httpd.conf", "w")
httpd.write(filedata)
httpd.close()
# restart apache
# os.system("sudo launchctl unload -w /System/Library/LaunchDaemons/org.apache.httpd.plist")
os.system("sudo /usr/local/bin/apachectl -k restart")
print(message)
