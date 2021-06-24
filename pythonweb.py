#!D:\python3.8\python.exe
import cgi

print("Content-Type:text/html \n\n")


print("<h1>Welcome to Python</h1>")
print("<h3>record inserted successfully</h3>")
print("<a href='http://localhost/hangman/form.html'>click</a>")
print("<input type='text' name='username'>")
print("<input type='submit'>")
import time
import datetime
import mysql.connector

form = cgi.FieldStorage()
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

username = form.getvalue("username")
conn = mysql.connector.connect(user="root",password="",host="localhost",database="my_python")
print("connected")
cur=conn.cursor()
cur.execute("insert into names(`username`,`Date`) values(%s,%s)",(username,timestamp))
conn.commit()
cur.close()
conn.close()