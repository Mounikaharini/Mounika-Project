import pymysql as p
db = p.connect(host="localhost",
               user="root",
               password="1234",
               database="pizza")
u = "mounika"
p = "21541"
import time
time = str(time.ctime())
cursor = db.cursor()
query = "Insert into login values('%s','%s','%s')"%(u,p,time)
cursor.execute(query)
db.commit()
db.close()
