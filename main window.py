import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tbp
from PIL import Image, ImageTk
from players import ShowInfo
from results import Results
from predict import Predict
from models import exist_users
from squad import Squad
from upcomingevents import UpcomingEvents
import MySQLdb


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


class Login(tbp.Window):
    def __init__(self, min_size):
        super().__init__()
        self.style.theme_use("cyborg")
        self.title("Club Results Management Platform")
        self.minsize(min_size[0], min_size[1])
        self.geometry(f"{min_size[0]}x{min_size[1]}")
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        # self.rowconfigure((0, 1, 2, 3, 4,5,6,7,8), weight=1, uniform="a")
        ttk.Label(self, text="Login", font=("Verdana", 20)).grid(row=0, column=1, pady=20)
        ttk.Label(self, text="username", font=("Verdana", 15)).grid(row=2, column=1, pady=10)
        user = ttk.Entry(self, width=50, font=("Verdana", 15))
        user.bind("<Return>", focus_next_widget)
        user.grid(row=3, column=1, pady=10)
        ttk.Label(self, text="password", font=("Verdana", 15)).grid(row=4, column=1, pady=10)
        acc = ttk.Entry(self, width=50, font=("Verdana", 15), show="*")
        acc.bind("<Return>", focus_next_widget)
        acc.grid(row=5, column=1, pady=10)

        def val():
            if user.get():
                password = exist_users(user.get())
                if (acc.get()) == str(password):
                    messagebox.showinfo("Success", "Logged in Successful")
                    Window(self)
                else:
                    messagebox.showwarning("Wrong", f"Incorrect UserName or Password")
            else:
                messagebox.showwarning("Wrong", f" user doesn't exists try again")
            user.delete(0, tk.END)
            acc.delete(0, tk.END)
        ttk.Button(self, text="log in", width=60,
                   command=val).grid(row=6, column=1, pady=10, sticky="nsew")
        tk.Button(self, text="Register", command=lambda: Register(self)).place(relx=0.45,
                                                                               rely=0.5,
                                                                               width=50, height=23)
        tk.Button(self, text="Cancel", command=lambda: self.withdraw()).place(relx=0.5,
                                                                              rely=0.5,
                                                                              width=50, height=23)

        # tk.Button(self, text="Register", command=lambda: Register(self)).grid(row=7, column=1, pady=10)
        self.mainloop()


class Window(tk.Toplevel):
    def __init__(self, close=None):
        super().__init__()

        if close is None:
            pass
        else:
            close.withdraw()
        self.title("Club Results Management Platform")
        # self.minsize(600, 600)
        self.geometry("1366x768")
        self.logo = Logo(self)
        self.logo.configure_destination()
        self.logo.logo_title()

        self.actions = Actions(self)
        self.actions.configure_destination()
        self.actions.action()

        self.description = Description(self)
        self.description.configure_destination()
        self.description.description()


class Logo(ttk.Frame):
    def __init__(self, parent=None):
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

        photo_path = Image.open("17vmy3h7.png")
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
        ttk.Button(self, text="View Squad", width=40, command=lambda: Squad()).grid(row=1, column=1, padx=10)
        ttk.Button(self, text="Predict", width=40, command=lambda: Predict()).grid(row=1, column=2, padx=10)
        ttk.Button(self, text="Upcoming Events", width=40,
                   command=lambda: UpcomingEvents()).grid(row=1, column=3, padx=10)
        ttk.Button(self, text="Add Player", width=40,
                   style="TButton", command=lambda: ShowInfo()).grid(row=1, column=4, padx=10)
        # ttk.Button(self, text="Logout", command=lambda: logout(Window())).place(x=1300, y=10, height=20)

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


class Register(tk.Toplevel):
    def __init__(self, lo):
        super().__init__()
        lo.withdraw()
        self.title("Register")
        self.minsize(1366, 768)
        self.form = Form(self)
        self.form.set_window()
        self.form.widgets()


class Form(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

    def widgets(self):
        ttk.Label(self, text="Register", font=("Verdana", 20)).grid(row=0, column=1)
        ttk.Label(self, text="First Name", font=("Verdana", 15)).grid(row=1, column=1, pady=20)
        first_name = ttk.Entry(self, font=("verdana", 15))
        first_name.bind("<Return>", focus_next_widget)
        first_name.grid(row=3, column=1, pady=10)
        ttk.Label(self, text="Second Name", font=("Verdana", 15)).grid(row=4, column=1, pady=10)
        last_name = ttk.Entry(self, font=("verdana", 15))
        last_name.bind("<Return>", focus_next_widget)
        last_name.grid(row=5, column=1, pady=10)
        ttk.Label(self, text="Email", font=("Verdana", 15)).grid(row=6, column=1, pady=10)
        email = ttk.Entry(self, font=("verdana", 15))
        email.bind("<Return>", focus_next_widget)
        email.grid(row=7, column=1, pady=10)
        ttk.Label(self, text="Password", font=("Verdana", 15)).grid(row=8, column=1, pady=10)
        password_1 = ttk.Entry(self, font=("verdana", 15), show="*")
        password_1.bind("<Return>", focus_next_widget)
        password_1.grid(row=9, column=1, pady=10)
        ttk.Label(self, text="Confirm Password", font=("Verdana", 15)).grid(row=10, column=1, pady=10)
        password_2 = ttk.Entry(self, font=("verdana", 15), show="*")
        password_2.bind("<Return>", focus_next_widget)
        password_2.grid(row=11, column=1, pady=10)
        ttk.Button(self, text="return",
                   width=55,
                   command=lambda: Login((600, 600))).grid(row=13, column=1)

        def f_name():
            if len(first_name.get()) > 3:
                return True

        def l_name():
            if len(first_name.get()) > 1:
                return True

        def check_em():
            if '@' or "gmail" or ".com" or ".info" or ".ac" in email.get():
                return True

        def password():
            if len(password_1.get()) > 3 and password_2.get() == password_1.get():
                return True

        def save_information():
            first_name_ = first_name.get()
            last_name_ = last_name.get()
            email_ = email.get()
            password_1_ = password_1.get()
            try:
                connection = MySQLdb.connect(
                                             hostp="localhost",
                                             user="root",
                                             password="Mmyjdm110793366490?",
                                             database="mkd")
                cursor = connection.cursor()
                cursor.execute("mkd;")
                if (f_name(first_name.get()) and l_name(last_name.get())
                        and password(password_1.get()) and check_em(email.get())):
                    cursor.execute("""
                    insert into users(first_name, last_name, email, password)
                    values(%s, %s, %s, %s);
                    """, (first_name_, last_name_, email_, password_1_))

                    messagebox.showinfo("Success", f"""User {first_name_} 
                     {last_name_} Created Successful""")

                    connection.commit()
                else:
                    messagebox.showwarning("invalid", "invalid input")
                    # if not f_name():
                    #     messagebox.showwarning("Wrong Input", f"""invalid First Name try again
                    #     """)
                    # elif not l_name():
                    #     messagebox.showwarning("Wrong Input", f"""{last_name_} invalid Last Name
                    #     try again
                    #     """)
                    # elif not password():
                    #     messagebox.showwarning("Wrong Input", f"""{password_1_} invalid password
                    #     try again
                    #     """)
                    # elif not check_em():
                    #     messagebox.showwarning("Wrong Input", f"""
                    #     {email_} invalid email try again
                    #     """)
                first_name.delete(0, tk.END)
                last_name.delete(0, tk.END)
                email.delete(0, tk.END)
                password_1.delete(0, tk.END)
                password_2.delete(0, tk.END)
                Window(None)

            except MySQLdb.Error as er:
                messagebox.showwarning("f", f"{er}")
        ttk.Button(self, text="Submit", width=55, command=lambda: Register()).grid(row=12, column=1, pady=10)

    def set_window(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")


window = Login((1366, 768))
window.mainloop()
