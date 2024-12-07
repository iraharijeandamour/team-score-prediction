import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import MySQLdb


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


connection = MySQLdb.connect(host="localhost",
                             user="root",
                             password="Mmyjdm110793366490?",
                             database="mkd")
cursor = connection.cursor()
cursor.execute("use mkd;")


def convert_to_binary(file_path):
    with open(file_path, "rb") as file:
        blob_data = file.read()
        return blob_data


def validate_id(player_id):
    player_id = int(player_id)
    if player_id > 0:
        return True


def validate_name(names):
    if len(names) > 2:
        return True


def validate_photo(photo):
    if photo:
        return True


def validate_position(position):
    if position in ["GoalKeeper", "Central Midfielder",
                    "Attacking Midfielder", "Right Winger",
                    "Central Back", "Left Winger", "Central Forward"]:
        return True


def validate_country(country):
    if country:
        return True


def save_data(player_id, names, position, country, photo):
    # cursor.execute("create database mkd;")
    # cursor.execute("""
    # create table players(player_id INT PRIMARY KEY, names varchar(100),
    # position varchar(50), country varchar(100), photo LONGBLOB);
    # """)
    query = "INSERT INTO players(player_id, names, position, country, photo) VALUES(%s, %s, %s,%s, %s);"
    if (validate_country(country.get()) and validate_position(position.get()) and
            validate_id(player_id.get()) and validate_photo(photo) and validate_name(names.get())):
        photo = convert_to_binary(photo.get())
        values = (player_id.get(), names.get(), position.get(), country.get(), photo)

        cursor.execute(query, values)
        messagebox.showinfo('Saved', f"Player {names} Added successfully")
        connection.commit()
        country.delete(0, tk.END)
        position.delete(0, tk.END)
        player_id.delete(0, tk.END)
        names.delete(0, tk.END)
    else:
        messagebox.showerror("Access Denied", " Failed To Add New Player Try Again")


def select_photo():
    photo_path = filedialog.askopenfilename()
    return photo_path


class ShowInfo(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Great")
        # self.minsize(600, 500)
        self.geometry("1366x768")
        # self.style.theme_use("superhero")

        self.add_player = AddPlayer(self)
        self.add_player.dest()
        self.add_player.add_widgets()

        # self.mainloop()


class AddPlayer(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dest()
        self.place(x=0, y=0, relwidth=1, relheight=1)

    def add_widgets(self):
        title = ttk.Label(self, text="Register Player", font="arial 20 bold", foreground="white")
        title.grid(row=0, column=1)
        name_label = ttk.Label(self, text="Name", font="courier 15")
        name_label.grid(row=1, column=1)

        name_value = ttk.Entry(self, width=50, font=("Times New Roman", 15))
        name_value.bind("<Return>", focus_next_widget)
        name_value.grid(row=2, column=1)

        position_label = ttk.Label(self, text="Position", font="courier 15")
        position_label.grid(row=3, column=1)

        positions = ["GoalKeeper", "Central Midfielder",
                     "Attacking Midfielder", "Right Winger",
                     "Central Back", "Left Winger", "Central Forward"]
        position_value = ttk.Combobox(self, width=50, font=("Times New Roman", 15))
        position_value['values'] = positions
        position_value.bind("<Return>", focus_next_widget)
        position_value.grid(row=4, column=1)

        number_label = ttk.Label(self, text="Shirt Number ", font="courier 15")
        number_label.grid(row=5, column=1)

        number_value = tk.Entry(self, width=50, font=("Times New Roman", 15))
        number_value.bind("<Return>", focus_next_widget)
        number_value.grid(row=6, column=1)

        number_label = ttk.Label(self, text="Photo ", font="courier 15")
        number_label.grid(row=7, column=1)
        photo_value = tk.Entry(self, width=50, font=("Times New Roman", 15))
        photo_value.bind("<Return>", focus_next_widget)
        photo_value.grid(row=8, column=1)

        def select(x):
            path = filedialog.askopenfilename()
            x.delete(0, tk.END)
            x.insert(0, path)

        # button = ttk.Button(self, text="browse file", command=select_photo)
        # button.place(x=835, y=280)
        tk.Button(self, text="browse", width=10,
                  command=lambda: select(photo_value)).grid(row=8, column=1, sticky="e")
        country_label = ttk.Label(self, text="Country", font="courier 15")
        country_label.grid(row=10, column=1)

        countries = ["Rwanda", "Nigeria", "England", "Japan", "Burundi", "DRC", "Zambia", "Mauritania"]
        country_value = ttk.Combobox(self, width=50, font=("Times New Roman", 15))
        country_value['values'] = countries
        country_value.bind("<Return>", focus_next_widget)
        country_value.grid(row=11, column=1)
        ttk.Button(self, text="Save", width=80,
                   command=lambda: save_data(number_value, name_value,
                                             position_value, country_value,
                                             photo_value)).grid(row=12, column=1, pady=10)
        ttk.Button(self, text="Add Player Stats", width=80, command=h).grid(row=13, column=1, pady=10)

    def dest(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12), weight=1, uniform="a")


def h():
    class AddPlayerStats(tk.Toplevel):
        def __init__(self, parent=None):
            super().__init__(parent)

            self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        def add_widgets(self):

            def save():
                stats_value = (
                    int(player_id.get()), float(player_goals.get()), float(player_assists.get()),
                    float(player_pcr.get()), float(player_ms.get()), float(player_tackles.get()), float(player_yc.get()),
                    float(player_rc.get())
                )
                if (player_id.get() and player_goals.get() and player_assists.get() and
                    player_pcr.get() and player_ms.get() and player_tackles.get()
                        and player_yc.get() and player_rc.get()):
                    cursor.execute("select player_id from player_stats;")
                    all_ids = []
                    ids = cursor.fetchall()
                    for id_ in ids:
                        all_ids.append(id_[0])
                    if int(player_id.get()) not in all_ids:
                        cursor.execute("""
                        insert into player_stats(
                        player_id, player_goals, player_assists, player_pcr, player_ms, 
                        player_tackles, player_yc, player_rc) values(%s, %s, %s, %s, %s, %s, %s, %s);
                        """, stats_value)
                        connection.commit()
                        player_id.delete(0, tk.END)
                        player_goals.delete(0, tk.END)
                        player_assists.delete(0, tk.END)
                        player_pcr.delete(0, tk.END)
                        player_ms.delete(0, tk.END)
                        player_tackles.delete(0, tk.END)
                        player_yc.delete(0, tk.END)
                        player_rc.delete(0, tk.END)
                        messagebox.showinfo("saved", "player stats saved successfully")
                    else:
                        messagebox.showwarning("invalid",
                                               """can't add player already exist, """)

                else:
                    messagebox.showwarning("invalid",
                                           """can't add player invalid inputs try again, """)
            player_tile = ttk.Label(self, text="Add Player Stats",
                                    font=("Verdana", 20))
            player_tile.grid(row=0, column=1, pady=3)

            player_id_label = ttk.Label(self, text="Player Shirt Number",
                                        font=("Verdana", 12))
            player_id_label.grid(row=1, column=1, pady=3)

            player_id = ttk.Entry(self, width=45)
            player_id.bind("<Return>", focus_next_widget)
            player_id.grid(row=2, column=1, pady=3)

            player_goals_label = ttk.Label(self, text="Goal Scored by Player",
                                           foreground="white", font=("Verdana", 12))
            player_goals_label.grid(row=3, column=1, pady=3)

            player_goals = ttk.Entry(self, width=45)
            player_goals.bind("<Return>", focus_next_widget)
            player_goals.grid(row=4, column=1, pady=3)

            player_assists_label = ttk.Label(self, text="Player Assists",
                                             foreground="white", font=("Verdana", 12))
            player_assists_label.grid(row=5, column=1, pady=3)

            player_assists = ttk.Entry(self, width=45)
            player_assists.bind("<Return>", focus_next_widget)
            player_assists.grid(row=6, column=1, pady=3)

            player_pcr_label = ttk.Label(self, text="Player Pass Completion rate",
                                         foreground="white", font=("Verdana", 12))
            player_pcr_label.grid(row=7, column=1, pady=3)

            player_pcr = ttk.Entry(self, width=45)
            player_pcr.bind("<Return>", focus_next_widget)
            player_pcr.grid(row=8, column=1, pady=3)

            player_mp_label = ttk.Label(self, text="Player Minutes Played",
                                        foreground="white", font=("Verdana", 12))
            player_mp_label.grid(row=9, column=1, pady=3)

            player_ms = ttk.Entry(self, width=45)
            player_ms.bind("<Return>", focus_next_widget)
            player_ms.grid(row=10, column=1, pady=3)

            player_tackles_label = ttk.Label(self, text="Player Tackles",
                                             foreground="white", font=("Verdana", 12))
            player_tackles_label.grid(row=11, column=1, pady=3)

            player_tackles = ttk.Entry(self, width=45)
            player_tackles.bind("<Return>", focus_next_widget)
            player_tackles.grid(row=12, column=1, pady=3)

            player_yellow_label = ttk.Label(self, text="Player Yellow Cards",
                                            foreground="white", font=("Verdana", 12))
            player_yellow_label.grid(row=13, column=1, pady=3)

            player_yc = ttk.Entry(self, width=45)
            player_yc.bind("<Return>", focus_next_widget)
            player_yc.grid(row=14, column=1, pady=3)

            player_red_label = ttk.Label(self, text="Player Red Cards",
                                         foreground="white", font=("Verdana", 12))
            player_red_label.grid(row=15, column=1, pady=3)

            player_rc = ttk.Entry(self, width=45)
            player_rc.bind("<Return>", focus_next_widget)
            player_rc.grid(row=16, column=1, pady=3)

            ttk. Button(self, text="save", width=15, command=save).grid(row=17, column=1, pady=3)

    aps = AddPlayerStats()
    aps.add_widgets()
