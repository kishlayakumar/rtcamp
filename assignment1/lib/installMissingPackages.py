import subprocess as insystem
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
  expect:
    return False

def installmissingPackages(OS):
  testVar = checkPHP()
  print testVar
  #if OS == "Fedora" or OS == "Centos":
installmissingPackages('Centos')    
