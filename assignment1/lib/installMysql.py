
import commands


def installMySqlOnREHL():
  output = commands.getoutput("sudo yum -y mysql")
  #output = commands.getoutput("sudo systemctl start mysqld")
def installMysqlOndebian():
  output = commands.getoutput("sudo apt-get install -y mysql")
  #output = commands.getoutput("sudo service mysql start")
