import pymysql

connection = pymysql.connect(host="localhost",user="vijay",database="practiceDB",password="py@007")

cursor = connection.cursor()

#sql = "CREATE TABLE STUDENT_ (STUDENT_ID INT (5) , NAME VARCHAR (10), AGE INT (10) ) "

sql_ = "INSERT INTO student_ (STUDENT_ID  , NAME , AGE  ) VALUES (1001,'VIJAY',25)"

print(f"{cursor.execute(sql_)}")

connection.commit()



