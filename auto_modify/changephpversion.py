import os

def replace(filename,search,replace):
    f = open(filename, "r+")
    content = f.read() 
    position = content.find(search) 
    f.seek(position,0) 
    f.write(replace)   
    f.close()

# # change php version
file_path = '/usr/local/etc/httpd/httpd.conf'
version = raw_input('what php version do you want? (current have 5 & 7):')
print(version)
if (version=='5'):
    print("change to version 5")
    replace(file_path,'LoadModule php7_module','#LoadModule php7_module') 
    replace(file_path,'#LoadModule php5_module','LoadModule php5_module ') 

if (version=='7'):
    print("change to version 7")
    replace(file_path,'#LoadModule php7_module','LoadModule php7_module ') 
    replace(file_path,'LoadModule php5_module','#LoadModule php5_module')

# restart apache
os.system("/usr/local/bin/apachectl -k restart")
os.system("open -a 'Google Chrome' http://mysql.local.com/phpinfo.php")

