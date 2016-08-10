import commands


def installPHPOnREHL():
  output = commands.getoutput("sudo yum install php php-mysql php-fpm")
  #output = commands.getoutput("sudo systemctl start php-fpm")
def installPHPOndebian():
  output = commands.getoutput("sudo apt-get install -y php-fpm php-mysql")
  output = command.getoutput("sudo ufw allow 'Nginx HTTP'")
  #output = commands.getoutput("sudo service ngnix start")


