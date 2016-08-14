import os

def startWordpressServices():
  os.system("service php7.0-fpm restart")
  os.system("service nginx restart")
  os.system("service mysql restart")
