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
    if testvarP == False:
      installPhp.installPHPOnREHL()
installmissingPackages('Centos')    
