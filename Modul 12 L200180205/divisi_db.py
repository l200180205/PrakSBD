import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector
from delete_divisi_db import delete_divisi

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perusahaan"
    )

c=db.cursor()

class divisi:
    def __init__(self, master):
        self.master = master
        self.master.title("Database Divisi")
        self.master.geometry('300x300')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Database Divisi", font=('Times', 16, 'bold'))
        l_divisi= Label(self.frame, text="Nama Divisi", font=('Times', 12))
        l_kode = Label(self.frame, text="Kode Divisi", font=('Times', 12))
        l_nama = Label(self.frame, text="Nama Karyawan", font=('Times', 12))
        
        
        title.grid(row=0, columnspan=4, pady=10)
        l_divisi.grid(row=1, column=0, sticky=W, padx=3)
        l_kode.grid(row=2, column=0, sticky=W, padx=3)
        l_nama.grid(row=3, column=0, sticky=W, padx=3)
       
        
        
        #Entry dan posisi
        self.e_divisi = Entry(self.frame, width=30)
        self.e_kode = Entry(self.frame, width=30)
        self.e_nama = Entry(self.frame, width=30)
        
        
        self.e_divisi.grid(row=1, column=1, sticky=W, padx=10)
        self.e_kode.grid(row=2, column=1, sticky=W, padx=10)
        self.e_nama.grid(row=3, column=1, sticky=W, padx=10)
    

        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_divisi)
        b_update = Button(self.frame, text="Update", command=self.update_divisi)
        b_show = Button(self.frame, text="Show", command=self.show_divisi)
        b_delete = Button(self.frame, text="Delete", command=self.delete_divisi)
        

        b_insert.grid(row=6, column=0, pady=10, ipadx=10)
        b_update.grid(row=6, column=1, pady=10, ipadx=10)
        b_show.grid(row=7, column=1, pady=10, ipadx=10)
        b_delete.grid(row=7, column=0, pady=10, ipadx=10)
        
    def insert_divisi(self):
        cursor = db.cursor()
        sql =f"INSERT INTO divisi (`divisi`,`kode`,`nama`,)VALUES('{self.e_divisi.get()}','{self.e_kode.get()}','{self.e_nama.get()}')"         
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
        
    
    def update_divisi(self):
        c = db.cursor()
        e1=self.e_divisi.get()
        e2=self.e_kode.get()
        e3=self.e_nama.get()
        sql =f"UPDATE divisi SET divisi=%s, nama=%s ,kode=%s"
        val = (e1,e2,e3)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_divisi(self):
        show = Tk()
        show.title("Data Divisi")
        Label(show, text="Divisi").grid(row=0, column=0, sticky=W)
        Label(show, text="Kode").grid(row=0, column=1, sticky=W)
        Label(show, text="Nama").grid(row=0, column=2, sticky=W)
        
        
        sql="select*from divisi"
        c.execute(sql)
        divisi = c.fetchall()

        for i in range(len(divisi)):
            for j in range(len(divisi[i])):
                teks=Entry(show)
                teks.grid(row=i+1,column=j)
                teks.insert(END,divisi[i][j])

    def delete_divisi(self):
        self.delete_divisi=Toplevel(self.master)
        self.UI=delete_divisi(self.delete_divisi)
