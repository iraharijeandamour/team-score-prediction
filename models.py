import MySQLdb
from tkinter import messagebox

connection = MySQLdb.connect(host="localhost",
                             user="root",
                             password="Mmyjdm110793366490?",
                             database="mkd")

cursor = connection.cursor()


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
                    "Attacking Midfielder", "Right Winger"
                    "Central Back", "Left Winger", "Central Forward"]:
        return True


def validate_country(country):
    if country:
        return True


def save_data(player_id, names, position, country, photo):
    try:
        cursor.execute("use mkd;")
        # cursor.execute("""
        # create table players(player_id INT PRIMARY KEY, names varchar(100),
        # position varchar(50), country varchar(100), photo LONGBLOB);
        # """)
        query = "INSERT INTO players(player_id, names, position, country, photo) VALUES(%s, %s, %s,%s, %s);"
        if (validate_country(country) and validate_position(position) and
                validate_id(player_id) and validate_photo(photo) and validate_name(names)):
            photo = convert_to_binary(photo)
            values = (player_id, names, position, country, photo)
            cursor.execute(query, values)
            messagebox.showinfo('Saved', f"Player {names} Added successfully")
            connection.commit()
        else:
            messagebox.showerror("Access Denied", " Failed To Add New Player Try Again")
    except MySQLdb.Error as err:
        print(f"There Is An Error {err}")


# save_data()

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
    if check_match(match) and check_teams(teams) and check_results(result):
        values = (match, teams, result)
        try:
            cursor.execute("use mkd;")
            query = """
            INSERT INTO results(match_type, teams_played, ft_result) values(%s, %s, %s);
            """
            cursor.execute(query, values)
            messagebox.showinfo("Success", "Match Added Successful")
            connection.commit()
        except MySQLdb.Error as Err:
            print(f"There is An Error {Err}")

    else:
        messagebox.showwarning("Invalid Input", "Can't Add Match Results Try Again")


def select_results():
    cursor.execute("use mkd;")
    cursor.execute("select result_date, match_type, teams_played, ft_result  from results;")
    return cursor.fetchall()


def exist_users(email):
    emails = []
    passwords = []
    cursor.execute("use mkd;")
    cursor.execute("select email, password from users;")
    users = cursor.fetchall()
    for em, pa in users:
        emails.append(em)
        passwords.append(pa)
    if email in emails:
        return passwords[emails.index(email)]
