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


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


def check_match(match):
    if match in ["Rwanda National League", "CAF Champions League",
                 "CAF Confederation Cup", "Friendly", "Rwanda Peace Cup"]:
        return True


def check_teams(teams):
    if "vs" or "VS" or "Vs" or "vS" in teams:
        return True


def check_results(result):
    if '-' or ':' in result:
        return True


def save_result(match, teams, result):
    if check_match(match.get()) and check_teams(teams.get()) and check_results(result.get()):
        values = (match.get(), teams.get().lower(), result.get())
        try:
            # cursor.execute("""create table results(result_id int AUTO_INCREMENT primary key,
            #  result_date DATETIME DEFAULT CURRENT_TIMESTAMP, match_type varchar(200),
            #  teams_played varchar(100), ft_result varchar(100));""")

            query = """
            INSERT INTO results(match_type, teams_played, ft_result) values(%s, %s, %s);
            """
            cursor.execute(query, values)
            messagebox.showinfo("Success", "Match Results Added Successful")
            connection.commit()

        except MySQLdb.Error as Err:
            print(f"There is An Error {Err}")

    else:
        messagebox.showwarning("Invalid Input", "Can't Add Match Results Try Again")
    match.delete(0, tk.END)
    teams.delete(0, tk.END)
    result.delete(0, tk.END)


class Results(tk.Toplevel):
    def __init__(self, cl=None):
        if cl is None:
            pass
        else:
            cl.withdraw()
        super().__init__()
        self.title("View Results")
        # self.minsize(500, 500)
        self.geometry("1366x768")

        self.match_result = MatchResults(self)
        self.match_result.conf()
        self.match_result.widgets()
        self.add_results = AddResult(self)


class MatchResults(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.5, relheight=1)

    def conf(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

    def widgets(self):

        table = ttk.Treeview(self, columns=("Date", "Match Type", "Teams", "FT Results"), show="headings")
        table.heading("Date", text="Date")
        table.heading("Match Type", text="Match Type")
        table.heading("Teams", text="Teams")
        table.heading("FT Results", text="FT Results")

        table.column("Date", width=100)
        table.column("Match Type", width=100)
        table.column("Teams", width=100)
        table.column("FT Results", width=100)

        def delete_selected_res():
            selected = table.selection()
            if selected:
                values_ = table.item(selected)["values"]
                date_ = values_[0]
                cursor.execute("delete from results where result_date=%s", (date_,))
                connection.commit()
                messagebox.showinfo("deleted", "results deleted successfully")
                show_all()
            else:
                messagebox.showwarning("warning", "no results selected")

        def hide():
            f = "Show All"
            show.configure(text=f)
            for ro in table.get_children():
                table.delete(ro)
            if f == "Show All":
                show.configure(command=show_all)

        def show_all():
            t = "Hide"
            show.configure(text=t)
            for row in table.get_children():
                table.delete(row)

            results_ = []
            cursor.execute("select result_date, match_type, teams_played, ft_result  from results;")
            results = cursor.fetchall()
            for all_results in results:
                results_.append(all_results)

            for date, match, teams, result in results:
                table.insert("", "end", values=(date, match, teams, result))
            if t == "Hide":
                show.configure(command=hide)
            else:
                show.configure(command=show_all)

        table.pack(expand=True, fill="both")

        def search():
            results_ = []
            for row in table.get_children():
                table.delete(row)
            if search_by.get() == "Date":
                cursor.execute("""select result_date, match_type, 
                teams_played, ft_result  from results 
                where result_date like %s;""", (f"%{search_value.get().lower()}%",))
                results = cursor.fetchall()
                for all_results in results:
                    results_.append(all_results)
                if results:
                    for date, match, teams, result in results:
                        table.insert("", "end", values=(date, match, teams, result))
                else:
                    messagebox.showwarning("empty", f"no results found on this {search_value.get()} ")
            elif search_by.get() == "Match Type":

                cursor.execute("""select result_date, match_type, 
                teams_played, ft_result  from results 
                where match_type like %s;""", (f"%{search_value.get()}%",))
                results = cursor.fetchall()
                for all_results in results:
                    results_.append(all_results)
                if results:
                    for date, match, teams, result in results:
                        table.insert("", "end", values=(date, match, teams, result))
                else:
                    messagebox.showwarning("empty", f"no results found corresponds {search_value.get()}")

            elif search_by.get() == "Results":
                cursor.execute("""select result_date, match_type, 
                teams_played, ft_result from results 
                where ft_result like %s;""", (f"%{search_value.get()}%",))
                results = cursor.fetchall()
                for all_results in results:
                    results_.append(all_results)
                if results:
                    for date, match, teams, result in results:
                        table.insert("", "end", values=(date, match, teams, result))
                else:
                    messagebox.showwarning("empty", f"no results found corresponds {search_value.get()}")

            elif search_by.get() == "Teams":
                cursor.execute("""select result_date, match_type, 
                teams_played, ft_result  from results 
                where teams_played like %s;""", (f"%{search_value.get()}%",))
                results = cursor.fetchall()
                for all_results in results:
                    results_.append(all_results)
                if results:
                    for date, match, teams, result in results:
                        table.insert("", "end", values=(date, match, teams, result))
                else:
                    messagebox.showwarning("empty", f"no results found corresponds {search_value.get()}")
            elif search_by.get() == "Search Any":
                cursor.execute("""select result_date, match_type, 
                               teams_played, ft_result  from results 
                               where result_date like %s or match_type 
                               like %s or teams_played like %s or ft_result like %s
                               ;""",
                               (f"%{search_value.get()}%", f"%{search_value.get()}%",
                                f"%{search_value.get()}%", f"%{search_value.get()}%",))

                results = cursor.fetchall()
                for all_results in results:
                    results_.append(all_results)
                if results:
                    for date, match, teams, result in results:
                        table.insert("", "end", values=(date, match, teams, result))
                else:
                    messagebox.showwarning("empty", f"no results found corresponds {search_value.get()}")

        ctk.CTkButton(self, text="Delete", command=delete_selected_res).place(x=30, y=550)
        values = ["Date", "Match Type", "Results", "Teams", "Search Any"]
        search_by = ctk.CTkComboBox(self, values=values, state="readonly")
        search_by.place(x=180, y=550)

        search_value = ctk.CTkEntry(self, bg_color="black")
        search_value.place(x=350, y=550)
        ctk.CTkButton(self, text="search", width=25, command=search).place(x=500, y=550)
        show = ctk.CTkButton(self, text="Show all", width=25, command=show_all)
        show.place(x=570, y=550)
        ctk.CTkOptionMenu(self)


class AddResult(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
        data = self.add_results()
        match = data[0]
        team = data[1]
        ft = data[2]

        ttk.Button(self, width=22, text="Save",
                   command=lambda: save_result(match, team, ft)).pack(pady=10)

    def add_results(self):
        match_ = ["Rwanda National League", "CAF Champions League",
                  "CAF Confederation Cup", "Friendly", "Rwanda Peace Cup"]
        ttk.Label(self, text="Add Match Results", font=("Verdana", 20)).pack()
        ttk.Label(self, text="Match Type", font=("Verdana", 15)).pack(pady=30)
        match_type = ttk.Combobox(self, width=50)
        match_type['values'] = match_
        match_type.pack()

        ttk.Label(self, text="Teams", font=("Verdana", 15)).pack(pady=10)
        team = ttk.Entry(self, width=50)
        team.bind("<Return>", focus_next_widget)
        team.pack()

        ttk.Label(self, text="FT Results", font=("Verdana", 15)).pack(pady=10)

        results = ttk.Entry(self, width=50)
        results.bind("<Return>", focus_next_widget)
        results.pack()

        return [match_type, team, results]
        #
        # button = ttk.Button(self, width=22, text="Save", command=lambda: save_result(match_type.get(), team.get(),
        #                                                                              results.get()))
        # button.pack(pady=10)
