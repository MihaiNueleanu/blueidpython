###################################################################
# Database connection layer
###################################################################
import MySQLdb

# Database parameters
host = "localhost"
sql_server_user = "root"
sql_server_password = "qwerty"
database = "blueid"

class CRUD:


    def login(self,username,password):
        db = MySQLdb.connect(host,sql_server_user ,sql_server_password,database)
        cursor = db.cursor()
        print "::::::::::::::: db connected :::::::::::::::"

        # sql = """CREATE TABLE IF NOT EXISTS users(uid VARCHAR(40) PRIMARY KEY,pw VARCHAR(255) NOT NULL,stat BOOLEAN NOT NULL DEFAULT FALSE);"""

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

                # Now print fetched result
                print "uid=%s,pwd=%s,stat=%d" % (uid,pwd,stat)
        except:
           print "Username not existent or data missing"
        db.close()