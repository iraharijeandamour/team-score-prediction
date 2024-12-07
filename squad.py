import tkinter
import tkinter as tk
from io import BytesIO
from tkinter import ttk, messagebox
import MySQLdb
import customtkinter as ctk
from PIL import Image

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
class Squad(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("MKD FC SQUAD")
        self.geometry("1366x768")
        self.bind("<F5>", self.refresh)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        ctk.CTkLabel(self, text="Squad For 2024-2025", text_color="white", font=("verdana", 20, "bold")).pack()
        self.widgets()

    @staticmethod
    def update_():
        cursor.execute("select * from players;")
        cursor.fetchall()

    def refresh(self):
        self.update_()

    def widgets(self):
        cursor.execute("select * from players;")
        data = cursor.fetchall()
        self.bind("<F5>", self.refresh)

        frame = tk.Frame(self)

        # Configure the grid columns
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        frame.place(x=0, y=100, relwidth=1, relheight=1)

        for count, row in enumerate(data):
            new_list = []
            image_data = row[4]
            image = Image.open(BytesIO(image_data))
            im = ttk.Frame(frame, height=300, width=400)
            im.columnconfigure((0, 1), weight=1, uniform="a")
            im.rowconfigure((0, 1, 3, 4, 5), weight=1, uniform="a")
            im.grid(row=count//5, column=count % 5, padx=10, pady=5, sticky="nsew")
            im.grid_propagate(False)

            def delete_player(lp):
                la = lp.cget("text").split()[0]
                if la:
                    cursor.execute("""delete from players where player_id=%s""", (int(la),))
                    connection.commit()
                    messagebox.showinfo("removed", "player removed from the squad")
                    self.widgets()
                else:
                    messagebox.showwarning("not exist", "player is not exists")

            def stats(lp):
                if new_list:
                    la = lp.cget("text").split()[0]
                    cursor.execute("""select * from 
                    player_stats where player_id=%s""", (int(la),))

                    cd = cursor.fetchall()
                    if cd:
                        k = tkinter.Toplevel()
                        k.title(f"{lp.cget("text").split()[1]} stats")
                        k.geometry("600x500")
                        for a, b, cc, d, e, f, g, h in cd:
                            tk.Label(k, text=f"{b} Goals", font=("Courier", 16, "bold")).pack(pady=5)
                            tk.Label(k, text=f"{cc} Assists", font=("Courier", 16, "bold")).pack(pady=5)

                            tk.Label(k, text=f"{d}% Pass Completion Rate", font=("Courier", 16, "bold")).pack(pady=5)
                            tk.Label(k, text=f"{e} Minutes Played", font=("Courier", 16, "bold")).pack(pady=5)

                            tk.Label(k, text=f"{f} Tackles", font=("Courier", 16, "bold")).pack(pady=5)
                    else:
                        messagebox.showwarning("no", "no stats found")

            tk.StringVar()
            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(200, 150))
            c = ttk.Label(im, text=f"{row[0]} {row[1]} {row[2]}", )
            c.grid(row=2, column=0, padx=20, columnspan=4)
            label = ctk.CTkLabel(im, image=ctk_image, text="")
            label.grid(row=0, column=0, rowspan=2, columnspan=3)
            new_list.append(c)
            ctk.CTkButton(im, text="view stats", fg_color="blue",
                          command=lambda ll=c: stats(ll)).grid(row=4, column=0, padx=20)
            ctk.CTkButton(im, text="remove", fg_color="red",
                          command=lambda lp=c: delete_player(lp)).grid(row=4, column=1, padx=15, ipadx=50)
