
import commands
import os

def installNginxOnREHL():
  output = commands.getoutput("sudo yum -y nginx")
  #output = commands.getoutput("sudo systemctl start nginx")
def installNginxOndebian():
  os.system("sudo apt-get install -y nginx")
  os.system("sudo ufw allow 'Nginx HTTP'")
  #output = commands.getoutput("sudo service ngnix start")

