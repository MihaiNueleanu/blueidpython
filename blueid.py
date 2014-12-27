###################################################################
# Database connection layer
###################################################################
import hashlib
import MySQLdb
from random import randint

# Database parameters
host = "localhost"
sql_server_user = "root"
sql_server_password = "qwerty"
database = "blueid"

class crud:


    def login(self,username,password):
        db = MySQLdb.connect(host,sql_server_user ,sql_server_password,database)
        cursor = db.cursor()
        print "::::::::::::::: db connected :::::::::::::::"

        # sql = """CREATE TABLE IF NOT EXISTS users(uid VARCHAR(40) PRIMARY KEY,pw VARCHAR(255) NOT NULL,stat BOOLEAN NOT NULL DEFAULT FALSE);INSERT INTO users (uid,pw,stat) VALUES (admin,%s,1) ;""" %

        self.username = username;
        self.password = password;
        sql = "SELECT * FROM blueid.users WHERE uid='%s';" % username

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                uid = row[0]
                pwd = row[1]
                stat = row[2]

            hashy = uid + pwd + str(randint(0, 999))
            print "this is the session key: " + hashlib.sha224(hashy).hexdigest()
            return hashlib.sha224(hashy).hexdigest()

        except:
           print "Username not existent or data missing"
        db.close()

    def initial_setup(self):
        db = MySQLdb.connect(host,sql_server_user ,sql_server_password,database)
        cursor = db.cursor()
        print "::::::::::::::: db setup :::::::::::::::"

        #sql = """CREATE TABLE IF NOT EXISTS blueid.users(uid VARCHAR(40) PRIMARY KEY,pw VARCHAR(255) NOT NULL,stat BOOLEAN NOT NULL DEFAULT FALSE);"""
        sql =  """INSERT INTO blueid.users(uid,pw,stat) VALUES ('admin','%s',1);""" % hashlib.sha224('1234').hexdigest()
        print sql
        try:
            #cursor.execute(sql)
            print "initial setup made"
        except:
           print "failed to execute"
        cursor.close()
        db.close()
