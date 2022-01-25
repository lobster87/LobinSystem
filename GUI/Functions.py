import mysql.connector as mysql
import GUI.userHome as userHome
import tkinter as tk
import os

def createUser(username, password, firstName, lastName):
    conn = mysql.connect(
        host= "localhost",
        user= os.environ.get("dbUser"),
        password= os.environ.get("dbPass"),
        database= "login"
    )

    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO users (username, password, firstName, lastName) 
        VALUES (
            '{username.get()}', 
            '{password.get()}', 
            '{firstName.get()}', 
            '{lastName.get()}'
            )"""
        )
    conn.commit()
    conn.close()

    username.delete(0,tk.END)
    password.delete(0,tk.END)
    firstName.delete(0,tk.END)
    lastName.delete(0,tk.END)

def login(username, password, frames):
    """ This function is to veryify login details """
    conn = mysql.connect(
        host= "localhost",
        user= os.environ.get("dbUser"),
        password= os.environ.get("dbPass"),
        database= "login"
    )

    cursor = conn.cursor()
    login_query = f"""
            SELECT firstName, lastName
            FROM users
            WHERE username='{username.get()}' 
            AND password='{password.get()}';
            """
    cursor.execute(login_query)

    row = cursor.fetchall() # store collected values

    if len(row) == 0: # if there are no compatible values 
        tk.messagebox.showinfo(
            'info', 
            'Incorrect username or password'
            )
        # Delete entered values
        username.delete(0,tk.END)
        password.delete(0,tk.END)
    else:
        """Change page """ # go to user homepage
        userHome.userHome(
            frames[0], 
            frames[1], 
            frames[2]
            )
    
    conn.commit()
    conn.close()



