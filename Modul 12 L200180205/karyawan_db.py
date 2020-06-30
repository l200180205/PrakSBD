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

class karyawan:
    def __init__(self, master):
        self.master = master
        self.master.title("karyawan")
        self.master.geometry('300x300')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Database Karyawan", font=('Times', 16, 'bold'))
        l_nama = Label(self.frame, text="Nama", font=('Times', 12))
        l_nik = Label(self.frame, text="NIK ", font=('Times', 12))
        l_alamat = Label(self.frame, text="Alamat", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_nama.grid(row=1, column=0, sticky=W, padx=3)
        l_nik.grid(row=2, column=0, sticky=W, padx=3)
        l_alamat.grid(row=3, column=0, sticky=W, padx=3)
        
        
        #Entry dan posisi
        self.e_nama = Entry(self.frame, width=30)
        self.e_nik = Entry(self.frame, width=30)
        self.e_alamat = Entry(self.frame, width=30)
        
        self.e_nama.grid(row=1, column=1, sticky=W, padx=10)
        self.e_nik.grid(row=2, column=1, sticky=W, padx=10)
        self.e_alamat.grid(row=3, column=1, sticky=W, padx=10)

        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_karyawan)
        b_update = Button(self.frame, text="Update", command=self.update_karyawan)
        b_show = Button(self.frame, text="Show", command=self.show_karyawan)

        b_insert.grid(row=5, column=0, pady=10, ipadx=10)
        b_update.grid(row=5, column=1, pady=10, ipadx=10)
        b_show.grid(row=7, column=1, pady=10, ipadx=10)
        
    def insert_karyawan(self):
        c = db.cursor()
        sql =f"INSERT INTO karyawan (`nama`,`nik`, `alamat`)VALUES('{self.e_id.get()}','{self.e_nama.get()}','{self.e_nik.get()}', '{self.e_alamat.get()}')"         
        c.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
    
    def update_karyawan(self):
        c = db.cursor()
        e1=self.e_nama.get()
        e2=self.e_nik.get()
        e3=self.e_alamat.get()
        sql =f"UPDATE karyawan SET nama=%s ,alamat=%s where nik=%s "
        val = (e1,e2,e3)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_karyawan(self):
        show = Tk()
        show.title("Data Karyawan")
        Label(show, text="Nama").grid(row=0, column=0, sticky=W)
        Label(show, text="NIK").grid(row=0, column=1, sticky=W)
        Label(show, text="Alamat").grid(row=0, column=2, sticky=W)
        

        
        sql="select*from karyawan"
        c.execute(sql)
        divisi = c.fetchall()

        for i in range(len(karyawan)):
            for j in range(len(karyawan[i])):
                teks=Entry(show)
                teks.grid(row=i+1,column=j)
                teks.insert(END,karyawan[i][j])
