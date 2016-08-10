
import fileinput

def configureEtcHost():
  file = open('/etc/hosts', 'a+')
  fileData = file.readlines()
  if "127.0.0.1 example.com\n" not in fileData:
    print("127.0.0.1 example.com\n" file = file)
  
  

configureEtcHost()



