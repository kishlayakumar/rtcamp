import commands


def installPHPOnREHL():
  output = commands.getoutput("sudo yum install php php-mysql php-fpm")
def installPHPOndebian():
  output = commands.getoutput("sudo apt-get install -y php-fpm php-mysql")


