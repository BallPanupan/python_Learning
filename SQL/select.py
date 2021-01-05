import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="it_data"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_test")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
