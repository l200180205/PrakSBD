import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE Perusahaan")

print("Database Perusahaan sukses dibuat")
