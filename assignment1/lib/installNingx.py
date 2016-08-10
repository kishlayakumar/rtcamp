
import commands


def installNginxOnREHL():
  output = commands.getoutput("sudo yum -y nginx")
  #output = commands.getoutput("sudo systemctl start nginx")
def installNginxOndebian():
  output = commands.getoutput("sudo apt-get install -y ngnix")
  output = command.getoutput("sudo ufw allow 'Nginx HTTP'")
  #output = commands.getoutput("sudo service ngnix start")

