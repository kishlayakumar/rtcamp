import os
import urllib
import urllib2
import shutil
def downloadWordpressZip():
  rootDir = "/usr/share/nginx/html/"
  urlTodownload = "http://wordpress.org/latest.zip"
  u = urllib2.urlopen(urlTodownload)
  meta = u.info()
  file_size = int(meta.getheaders("Content-Length")[0])
  print ("Downloading: %s Bytes: %s" % ('wordpress', file_size))
  urllib.urlretrieve(urlTodownload, rootDir + '/latest.zip')
  os.chdir(rootDir)
  if (os.path.exists('wordpress') == True):
    shutil.rmtree('wordpress')
  if (os.path.exists("latest.zip") == True):
    print ("file present")
    os.system('unzip latest.zip')
    print ("Extracted in Current Directory")
  else :
    print ("file not found")
    exit(0)
  


downloadWordpressZip()
