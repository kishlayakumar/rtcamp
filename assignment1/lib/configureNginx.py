from __future__ import print_function
import fileinput
import sys
from tempfile import mkstemp
from shutil import move
from os import remove, close, system
def configFileEdit(filename):
  fileName = "/etc/nginx/conf.d/" + filename + ".conf"
  file = open(fileName, 'w')
  print("server {\n " +
        "listen       80 default_server;\n"+
        "listen       [::]:80 default_server;\n"+
        "server_name  " +filename+";\n"+
        "root         /usr/share/nginx/html/wordpress;\n"+
        "index index.php index.html index.htm;\n"+\
        "include /etc/nginx/default.d/*.conf;\n"+\
        "location ~ \.php$ {\n" +\
        "  try_files $uri =404;\n"+\
        "  fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;\n" +\
        "   fastcgi_index index.php;\n" +\
        "   fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;\n" +\
        "   include fastcgi_params;\n" +
        "}\n}", file = file)

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
              if "8080" not in line:
                new_file.write(line.replace(pattern, subst))
              else:
                new_file.write(line)
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
def configureMainFile():
    fileTosearch = "/etc/nginx/nginx.conf"
    fileToSearch_1 = "/etc/nginx/sites-available/default"
    replace(fileTosearch, "80", "8080")
    replace(fileToSearch_1, "80", "8080 ")
    system("chmod 777 /etc/nginx/nginx.conf")
    system("chmod 777 /etc/nginx/sites-available/default")
