import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perusahaan"
)

cursor = mydb.cursor()

query = """
CREATE TABLE presensi
(
    Nama VARCHAR (45),
    Izin INT(10),
    Keterangan VARCHAR(100),
    Hadir INT(45)
)
"""

cursor.execute(query)

print("Table presensi sukses dibuat")
