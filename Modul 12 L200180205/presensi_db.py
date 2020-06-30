import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perusahaan"
    )

c=db.cursor()

class presensi:
    def __init__(self, master):
        self.master = master
        self.master.geometry('450x250')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Pendataan Presensi Karyawan", font=('Times', 16, 'bold'))
        l_nama = Label(self.frame, text="Nama Karyawan", font=('Times', 12))
        l_izin = Label(self.frame, text="Izin", font=('Times', 12))
        l_keterangan = Label(self.frame, text="Keterangan", font=('Times', 12))
        l_hadir= Label(self.frame, text="Hadir", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_nama.grid(row=1, column=0, sticky=W, padx=3)
        l_izin.grid(row=2, column=0, sticky=W, padx=3)
        l_keterangan.grid(row=3, column=0, sticky=W, padx=3)
        l_hadir.grid(row=4, column=0, sticky=W, padx=3)
        
        
        #Entry dan posisi
        self.e_nama = Entry(self.frame, width=30)
        self.e_izin = Entry(self.frame, width=30)
        self.e_keterangan = Entry(self.frame, width=30)
        self.e_hadir = Entry(self.frame, width=30)
        
        self.e_nama.grid(row=1, column=1, sticky=W, padx=10)
        self.e_izin.grid(row=2, column=1, sticky=W, padx=10)
        self.e_keterangan.grid(row=3, column=1, sticky=W, padx=10)
        self.e_hadir.grid(row=4, column=1, sticky=W, padx=10)

        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_presensi)
        b_update = Button(self.frame, text="Update", command=self.update_presensi)
        b_show = Button(self.frame, text="Show", command=self.show_presensi)

        b_insert.grid(row=5, column=0, pady=10, ipadx=10)
        b_update.grid(row=5, column=1, pady=10, ipadx=10)
        b_show.grid(row=5, column=2, pady=10, ipadx=10)
        
    def insert_presensi(self):
        c = db.cursor()
        sql =f"INSERT INTO peminjaman (`namaFK`,`izinFK`,`keterangan`, `hadir`)VALUES('{self.e_nama.get()}','{self.e_izin.get()}','{self.e_keterangan.get()}', '{self.e_hadir.get()}')"         
        c.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
    
    def update_presensi(self):
        c = db.cursor()
        e1=self.e_nama.get()
        e2=self.e_hadir.get()
      
        sql =f"UPDATE Presensi SET hadirFK=%s where namaFK=%s"
        val = (e1,e2)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_presensi(self):
        presensi = Tk()
        presensi.title("Presensi Karyawan")
        Label(presensi, text="Nama").grid(row=0, column=0, sticky=W)
        Label(presensi, text="izin").grid(row=0, column=1, sticky=W)
        Label(presensi, text="Keterangan").grid(row=0, column=2, sticky=W)
        Label(presensi, text="Hadir").grid(row=0, column=3, sticky=W)
        
        
        sql="select*from peminjaman_pengembalian"
        c.execute(sql)
        presensi = c.fetchall()

        for i in range(len(presensi)):
            for j in range(len(presensi[i])):
                teks=Entry(presensi)
                teks.grid(row=i+1,column=j)
                teks.insert(END,presensi[i][j])
