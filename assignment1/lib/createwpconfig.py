from __future__ import print_function
import fileinput
import sys
from tempfile import mkstemp
from shutil import move
from os import remove, close, system


def configFile(dbname):
  dbname = dbname + "_db"
  sampleconfigFile = "/usr/share/nginx/html/wordpress/wp-config-sample.php"
  configFile = "/usr/share/nginx/html/wordpress/wp-config.php"
  with open(configFile,'w') as new_file:
    with open(sampleconfigFile) as old_file:
      for line in old_file:
        if "database_name_here" in line:
          new_file.write(line.replace('database_name_here', dbname))
        elif "username_here" in line:
          new_file.write(line.replace('username_here', 'iiiiiiiiiiiiriiasasasedoodasdt'))
        elif "password_here" in line:
          new_file.write(line.replace('password_here', 'xxxxxxxxxxxx'))
        else:
          new_file.write(line)  
configFile('example')
