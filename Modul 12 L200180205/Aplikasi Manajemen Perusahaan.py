import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector
from karyawan_db import karyawan
from divisi_db import divisi
from presensi_db import presensi


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perusahaan"
    )

c=db.cursor()

root = tk.Tk()

def CRUD():
    UI=FPage(root)
    cursor=db.cursor()

class FPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.config(bg = 'white')
        self.frame = Frame(self.master, bg = 'white')
        self.frame.pack()
        
        title = Label(self.frame, text='SELAMAT DATANG', font=('Times', 18, 'bold'))
        title.pack()
        title2 = Label(self.frame, text='Pilih Menu', font=('Times', 14))
        title2.pack(pady=20)
        btnKaryawan = Button(self.frame, text="Karyawan", font=(18), command=self.karyawan)
        btnKaryawan.pack(anchor=CENTER, pady=10, ipadx=9)
        btnDivisi = Button(self.frame, text="Divisi", font=(18), command=self.divisi)
        btnDivisi.pack(anchor=CENTER, pady=10, ipadx=20)
        btnPresensi = Button(self.frame, text="Presensis", font=(18), command=self.presensi)
        btnPresensi.pack(anchor=CENTER, pady=10, ipadx=15)

    def karyawan(self):
        self.karyawanr=Toplevel(self.master)
        self.UI=karyawan(self.karyawan)

    def divisi(self):
        self.divisi=Toplevel(self.master)
        self.UI=divisi(self.divisi)

    def presensi(self):
        self.presensi=Toplevel(self.master)
        self.UI=presensi(self.presensi)

    


CRUD()
