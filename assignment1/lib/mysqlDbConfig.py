import MySQLdb as MS



def createdb(nameOfDb):
  db1 = MS.connect(host="localhost",user="root",passwd="root@123")
  cursor = db1.cursor()
  sql = 'CREATE DATABASE ' + nameOfDb + "_db"
  cursor.execute(sql)

