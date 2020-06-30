import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perusahaan"
)

cursor = mydb.cursor()

query = """
CREATE TABLE karyawan
(
    nik INT(10),
    nama VARCHAR(100),
    alamat VARCHAR(100)
)
"""

cursor.execute(query)

print("Table karyawan sukses dibuat")
