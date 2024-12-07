import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def prediction(a, b, c, d, e, f, g, h, i, j):
    if (not a.get() or not b.get() or not c.get()
            or not d.get() or not e.get() or not f.get()
            or not g.get() or not h.get() or not i.get() or not j.get()):
        messagebox.showwarning("invalid", "can't predict invalid input")
    else:
        aa = float(a.get())
        bb = float(b.get())
        cc = float(c.get())
        dd = float(d.get())
        ee = float(e.get())
        ff = float(f.get())
        gg = float(g.get())
        hh = float(h.get())
        ii = float(i.get())
        jj = j.get()
        a.delete(0, tk.END)
        b.delete(0, tk.END)
        c.delete(0, tk.END)
        d.delete(0, tk.END)
        e.delete(0, tk.END)
        f.delete(0, tk.END)
        g.delete(0, tk.END)
        h.delete(0, tk.END)
        i.delete(0, tk.END)
        j.delete(0, tk.END)

        df = pd.read_csv("teamstats.csv")
        # selecting main features
        df = df[
            ["goals", "xGoals", "shots", "shotsOnTarget", "ppda", "fouls", "corners",
             "yellowCards", "redCards", "result"]]
        # create train data and test data
        x = df[["goals", "xGoals", "shots", "shotsOnTarget", "ppda", "fouls", "corners", "yellowCards", "redCards"]]
        y = df['result']
        """Creating X, Y test and train data"""
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=20)
        model = LogisticRegression(max_iter=1000)
        predicted = model.fit(x_train, y_train)
        result = predicted.predict([[aa, bb, cc, dd, ee, ff, gg, hh, ii]])[0]
        if result == 'L':
            messagebox.showinfo("success", f"MKD FC Win")
        elif result == 'W':
            messagebox.showinfo("success", f"{jj} Win")
        else:
            messagebox.showinfo("success", "Draw")


def next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"


class Predict(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Predict")
        # self.minsize(600, 500)
        self.geometry("1366x768")
        self.form = Form(self)
        self.form.config()
        self.info = Info(self)
        self.info.widgets()


class Form(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=0.6)
        ttk.Label(self, text="Fill Info Below To Predict The Match Result",
                  font=("Verdana", 20)).grid(row=1, column=1)
        ttk.Label(self, text="goals per match",
                  font=("Verdana", 15)).grid(row=2, column=0)

        goals = ttk.Entry(self, width=50)
        goals.bind("<Return>", next_entry)
        goals.grid(row=3, column=0, pady=10)

        ttk.Label(self, text="goal against per match",
                  font=("Verdana", 15)).grid(row=2, column=1)
        xgoal = ttk.Entry(self, width=50)
        xgoal.grid(row=3, column=1, pady=10)
        xgoal.bind("<Return>", next_entry)

        ttk.Label(self, text="shots per match",
                  font=("Verdana", 15)).grid(row=2, column=2)
        shots = ttk.Entry(self, width=50)
        shots.grid(row=3, column=2, pady=10)
        shots.bind("<Return>", next_entry)

        ttk.Label(self, text="shots on target per match", font=("Verdana", 15)).grid(row=4, column=0)
        shot_on_target = ttk.Entry(self, width=50)
        shot_on_target.grid(row=5, column=0, pady=10)
        shot_on_target.bind("<Return>", next_entry)

        ttk.Label(self, text="pass per defensive action",
                  font=("Verdana", 15)).grid(row=4, column=1)
        ppda = ttk.Entry(self, width=50)
        ppda.grid(row=5, column=1, pady=10)
        ppda.bind("<Return>", next_entry)

        ttk.Label(self, text="fouls per match",
                  font=("Verdana", 15)).grid(row=4, column=2)
        fouls = ttk.Entry(self, width=50)
        fouls.grid(row=5, column=2, pady=10)
        fouls.bind("<Return>", next_entry)

        ttk.Label(self, text="corners per match",
                  font=("Verdana", 15)).grid(row=6, column=0)
        corners = ttk.Entry(self, width=50)
        corners.grid(row=7, column=0, pady=10)
        corners.bind("<Return>", next_entry)

        ttk.Label(self, text="yellow cards per match",
                  font=("Verdana", 15)).grid(row=6, column=1)
        yellow_crds = ttk.Entry(self, width=50)
        yellow_crds.grid(row=7, column=1, pady=10)
        yellow_crds.bind("<Return>", next_entry)

        ttk.Label(self, text="red cards per game",
                  font=("Verdana", 15)).grid(row=6, column=2)
        red_cards = ttk.Entry(self, width=50)
        red_cards.grid(row=7, column=2, pady=10)
        red_cards.bind("<Return>", next_entry)

        ttk.Label(self, text="Opponent Name",
                  font=("Verdana", 15)).grid(row=8, column=1)
        team = ttk.Entry(self, width=50)
        team.bind("<Return>", next_entry)
        team.grid(row=9, column=1)

        ttk.Button(self, text="Predict Full Time Results",
                   width=50,
                   command=lambda: prediction(goals, xgoal, shots,
                                              shot_on_target, ppda, fouls,
                                              corners, yellow_crds,
                                              red_cards, team)).grid(row=10, column=1, pady=20)

    def config(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")


class Info(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely=0.6, relwidth=1, relheight=0.4)
        # self.title("Brief Results Details")

    def widgets(self):
        data = "The Results Which Will Be Predicted Based On MKD FC Past Results"
        data_1 = "It Is not Probably Real, It can Change Based On Game Features"
        data_2 = "It's Powered By AI Algorithm By Jean D Amour, Junior Data Scientist "
        ttk.Label(self, text=data, font=("Courier", 20)).pack()
        ttk.Label(self, text=data_1, font=("Courier", 20)).pack()
        ttk.Label(self, text=data_2, font=("Courier", 20)).pack()
