from cgitb import text
import tkinter as tk
from turtle import position
from constVariables import *
from GUI.Functions import createUser
import GUI.homepage as login
class createNewUser:
    def __init__(self, currentFrame, chosenFrame, frame):
        # initiate the frame
        self.frame = frame
        currentFrame.forget()
        chosenFrame.pack(fill='both', expand=True)
        self.shown()
    
    def shown(self):
        title = tk.Label(
            self.frame[1], 
            text="Create User",
            bg='red',
            font='30'
            )
        titleWidth = 0.25*windowWidth
        titlex = (windowWidth*0.5) - (titleWidth*0.5)
        title.place(width=titleWidth, x=titlex, y=50)

        elementWidth = 0.25*windowWidth
        # username
        userLabel = tk.Label(
            self.frame[1], 
            text='Username:', 
            bg='white',
            anchor='w'
            )
        userLabel.place(
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=75
            )
        userEntry = tk.Entry(self.frame[1])
        userEntry.place(
            width=elementWidth,
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=100
            )
        # password
        passLabel = tk.Label(
            self.frame[1], 
            text='Password:', 
            bg='white',
            anchor='w'
            )
        passLabel.place(
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=125
            )
        passEntry = tk.Entry(self.frame[1])
        passEntry.place(
            width=elementWidth,
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=150
            )
        # firstname
        firstLabel = tk.Label(
            self.frame[1], 
            text='First name:', 
            bg='white',
            anchor='w'
            )
        firstLabel.place(
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=175
            )
        firstEntry = tk.Entry(self.frame[1])
        firstEntry.place(
            width=elementWidth,
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=200
            )
        # last name
        lastLabel = tk.Label(
            self.frame[1], 
            text='Last name:', 
            bg='white',
            anchor='w'
            )

        lastLabel.place(
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=225
            )
        lastEntry = tk.Entry(self.frame[1])
        lastEntry.place(
            width=elementWidth,
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=250
            )

        # submit button
        submit = tk.Button(
            self.frame[1],
            text='Submit', 
            command=lambda: createUser(
                userEntry, 
                passEntry, 
                firstEntry, 
                lastEntry,
            )
        )
        submit.place(
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=275
        )

        # return to login page
        loginButton = tk.Button(
            self.frame[1],
            text='Login', 
            command=lambda: login.loginPage(
                self.frame[1], 
                self.frame[0], 
                self.frame
            )
        )
        loginButton.place(
            x=(windowWidth*0.5) - (titleWidth*0.5),
            y=325
        )
