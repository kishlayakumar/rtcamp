
import commands
import os


def installMySqlOnREHL():
  output = commands.getoutput("sudo yum -y mysql")
  #output = commands.getoutput("sudo systemctl start mysqld")
def installMysqlOndebian():
  output = os.system("sudo apt-get install -y mysql-server")
  #output = commands.getoutput("sudo service mysql start")
