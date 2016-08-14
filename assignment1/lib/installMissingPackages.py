import subprocess as insystem
import installMysql
import installNingx
import installPhp





def checkPHP():
  try:
    insystem.check_call(['php', '-v'])
    return True
  except:
    return False
def checkMysql():
  try:
    insystem.check_call(['mysql', '-V'])
    return True
  except:
    return False
def checkNginx():
  try:
    insystem.check_call(['which', 'nginx'])
    return True
  except: 
     return False

def installmissingPackages(OS):
  testVarM = checkMysql()
  testVarN = checkNginx()
  testVarP = checkPHP()
  
  if OS == "Fedora" or OS == "Centos":
    if testVarM == False:
      installMysql.installMySqlOnREHL()
    if testVarN == False:
      installNingx.installNginxOnREHL()
    if testVarP == False:
      installPhp.installPHPOnREHL()
  elif OS == "debian" or OS == "Ubuntu":
    if testVarM == False:
      print ("Mysql not found")
      print ("Installing Mysql")
      installMysql.installMysqlOndebian()
    if testVarN == False:
      print("Nginx not found")
      print ("Installing Nginx")
      installNingx.installNginxOndebian()
    if testVarP == False:
      print("Php not found")
      print("Installing php")
      installPhp.installPHPOndebian()
