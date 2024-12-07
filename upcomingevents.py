import customtkinter as c
import tkinter as tk
from tkinter import ttk, messagebox
import MySQLdb
import customtkinter as ctk
connection = MySQLdb.connect(host="localhost",
                             user="root",
                             password="Mmyjdm110793366490?",
                             database="mkd")
cursor = connection.cursor()
cursor.execute("use mkd;")


class UpcomingEvents(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Upcoming Events")
        self.geometry("500x300")
        ttk.Label(self, text="Events Available", font=("Verdana", 20, "bold")).pack(pady=10)
        ttk.Label(self, text="No Events Available").place(relx=0.4, rely=0.4, relwidth=0.3, height=20)
