import tkinter as tk
from tkinter import ttk, messagebox
import MySQLdb


class Regist(tk.Toplevel):
    def __init__(self, par=None):
        super().__init__()
        # par.withdraw()
        self.title("Register")
        self.minsize(600, 600)
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
        first_name = ttk.Entry(self, font=("verdana", 20))
        first_name.grid(row=3, column=1, pady=10)
        ttk.Label(self, text="Second Name", font=("Verdana", 15)).grid(row=4, column=1, pady=10)
        last_name = ttk.Entry(self, font=("verdana", 20))
        last_name.grid(row=5, column=1, pady=10)
        ttk.Label(self, text="Email", font=("Verdana", 15)).grid(row=6, column=1, pady=10)
        email = ttk.Entry(self, font=("verdana", 20))
        email.grid(row=7, column=1, pady=10)
        ttk.Label(self, text="Password", font=("Verdana", 15)).grid(row=8, column=1, pady=10)
        password_1 = ttk.Entry(self, font=("verdana", 20))
        password_1.grid(row=9, column=1, pady=10)
        ttk.Label(self, text="Confirm Password", font=("Verdana", 15)).grid(row=10, column=1, pady=10)
        password_2 = ttk.Entry(self, font=("verdana", 20))
        password_2.grid(row=11, column=1, pady=10)
        ttk.Button(self, text="return", width=30, command="").grid(row=13, column=1)

        def f_name():
            if len(first_name.get()) > 3:
                return True

        def l_name():
            if len(first_name.get()) > 1:
                return True
            pass

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
                connection = MySQLdb.connect(host="localhost",
                                             user="root",
                                             password="Mmyjdm110793366490",
                                             database="mkd")
                cursor = connection.cursor()
                cursor.execute("use mkd;")
                if f_name() and l_name() and password() and check_em():
                    cursor.execute("""
                    insert into users(first_name, last_name, email, password)
                    values(%s, %s, %s, %s);
                    """, (first_name_, last_name_, email_, password_1_))

                    messagebox.showinfo("Success", f"""User {first_name_} 
                     {last_name_} Created Successful""")

                    connection.commit()
                else:
                    if not f_name():
                        messagebox.showerror("Wrong Input", f"""{first_name_} invalid First Name
                        try again
                        """)
                    elif not l_name():
                        messagebox.showerror("Wrong Input", f"""{last_name_} invalid Last Name
                        try again
                        """)
                    elif not password():
                        messagebox.showerror("Wrong Input", f"""{password_1_} invalid password
                        try again
                        """)
                    elif not check_em():
                        messagebox.showerror("Wrong Input", f"""
                        {email_} invalid email try again
                        """)
                    first_name.delete(0, tk.END)
                    last_name.delete(0, tk.END)
                    email.delete(0, tk.END)
                    password_1.delete(0, tk.END)
                    password_2.delete(0, tk.END)

            except MySQLdb.Error as er:
                pass
        ttk.Button(self, text="Submit", width=55, command=save_information).grid(row=12, column=1, pady=10)

    def set_window(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
