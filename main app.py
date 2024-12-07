import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tbp
from PIL import Image, ImageTk
from players import ShowInfo
from results import Results
from predict import Predict


class Window(tbp.Window):
    def __init__(self, min_size):
        super().__init__()
        self.style.theme_use("superhero")
        self.title("Club Results Management Platform")
        self.minsize(min_size[0], min_size[1])
        self.geometry(f"{min_size[0]}x{min_size[1]}")

        self.logo = Logo(self)
        self.logo.configure_destination()
        self.logo.logo_title()

        self.actions = Actions(self)
        self.actions.configure_destination()
        self.actions.action()

        self.description = Description(self)
        self.description.configure_destination()
        self.description.description()

        # self.mainloop()


class Logo(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=0.2)

    def logo_title(self):
        text = """
        Mkd FootBall Club Results and Score Prediction Management System
        For Secure And Sustainable Development
        """
        why = """Mkd Fc Is My Future Business Dream  Mkd Stands for MUKASINE DATIVE My Lovely Mother"""
        ttk.Label(self, text=text,
                  font=("Verdana", 20)).place(x=170, y=0)

        photo_path = Image.open("van.jpg")
        photo = ImageTk.PhotoImage(photo_path)
        photo_label = tk.Label(self, image=photo)
        photo_label.image = photo
        photo_label.place(x=0, y=5)
        ttk.Label(self, text=why, font=("Verdana", 15)).grid(row=3, column=1, columnspan=2, pady=5)

    def configure_destination(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")


class Actions(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0, rely=0.3, relwidth=1, relheight=0.6)

    def action(self):
        ttk.Label(self, text="Actions",
                  background="",
                  foreground="white",
                  font=("Fixedsys", 30),
                  width=40,
                  anchor='center'
                  ).grid(row=0, column=2)

        #  styling a Button
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 18))

        ttk.Button(self, text="View Results", width=40,
                   command=lambda: Results()).grid(row=1, column=0, padx=10)
        ttk.Button(self, text="View Squad", width=40).grid(row=1, column=1, padx=10)
        ttk.Button(self, text="Predict", width=40, command=lambda: Predict()).grid(row=1, column=2, padx=10)
        ttk.Button(self, text="Upcoming Events", width=40).grid(row=1, column=3, padx=10)
        ttk.Button(self, text="Add Player", width=40,
                   style="TButton", command=lambda: ShowInfo()).grid(row=1, column=4, padx=10)

    def configure_destination(self):
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")


class Description(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0, rely=0.6, relwidth=1, relheight=0.6)

    def description(self):
        messages = """
        This project is determined by Enthusiast Junior Data Scientist, IRAHARI Jean D Amour,
        He's planning to land football club in rwanda, He thinks of forming football academy, 
        where talent will be recognised based on Data science application.  
        """
        ttk.Label(self,
                  text=messages,
                  font=("Verdana", 18)).grid(
                  row=0, column=2, columnspan=4,
                  rowspan=3, sticky="nsew",)

    def configure_destination(self):
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")


window = Window((600, 600))
window.mainloop()
