import commands
import lib.checkOs as os
import lib.installMissingPackages as imp
import lib.configureNginx as confNginx
import lib.startServices as startServices
import lib.mysqlDbConfig as mysqlDbConfig
import lib.createwpconfig as createwpconfig
osName = os.checkOs()
imp.installmissingPackages(osName)
websiteName = raw_input("Please Enter Your website name:")
confNginx.configureMainFile()
confNginx.configFileEdit(websiteName)
startServices.startWordpressServices()
dbName = websiteName.aplt('.')[0]
mysqlDbConfig.createdb(dbName)
createwpconfig.configFile(dbname)
