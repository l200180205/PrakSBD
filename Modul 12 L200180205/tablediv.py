import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perusahaan"
)

cursor = mydb.cursor()

query = """
CREATE TABLE divisi
(
    divisi VARCHAR(100),
    kode  INT(10),
    nama VARCHAR(100)
)
"""

cursor.execute(query)

print("Table divisi sukses dibuat")
