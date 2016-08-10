import print_function
import shutil
def configFileEdit():
  file = open("/etc/php-fpm.d/www.conf", "r+")
  file1 = open("/tmp/www.conf", "w")
  count = 0
  for line in file:

   if "listen = " in line:
     print ("listen = /var/run/php-fpm/php-fpm.sock", file =file1)
   elif "user = " in line:

     print ("user = nginx", file = file1)
   elif "group = " in line:
     if (count == 0):
       print ("group = nginx", file=file1)
       count +=1
   else:
     print (line, file=file1)
  shutil.move('/tmp/www.conf', '/etc/php-fpm.d/www.conf')
configFileEdit()
~               
