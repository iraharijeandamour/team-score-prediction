"""
Light Themes
"""
"""
Cosmo

Flatly

Journal

Litera

Lumen

Minty

Pulse

Sandstone

United

Yeti

Morph

Dark Themes
Darkly

Cyborg

Superhero

Solar
"""
# from random import choice
# import MySQLdb
# connection = MySQLdb.connect(host="localhost",
#                              user="root",
#                              password="Mmyjdm110793366490?",
#                              database="mkd")
# cursor = connection.cursor()
# cursor.execute("use mkd;")
# cursor.execute("select * from players;")
# data = cursor.fetchall()
# print(choice((12, 45, 67)))
# # for i, row in enumerate(data):
#     # print(row[0], row[1], row[2], row[3], i)



import tkinter as tk
from tkinter import ttk, messagebox
import MySQLdb
import customtkinter as ctk
from io import BytesIO
from PIL import Image, ImageTk

# Connect to the database
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    password="Mmyjdm110793366490?",
    database="mkd"
)
cursor = connection.cursor()
cursor.execute("use mkd;")

# Main window class
cursor.execute("select player_id from player_stats;")
all_ids = []
ids = cursor.fetchall()
for id_ in ids:
    all_ids.append(id_[0])
print(all_ids)