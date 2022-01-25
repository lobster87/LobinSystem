from cgitb import text
from re import X
import tkinter as tk
from constVariables import *
from GUI.createUser import createNewUser
import GUI.Functions as functions

class loginPage():
    def __init__(self, currentFrame, chosenFrame, frame):
        # initiate the frame
        self.frame = frame
        currentFrame.forget()
        chosenFrame.pack(fill='both', expand=1)
        self.shown()
    
    def shown(self):
        # Title
        title = tk.Label(
            self.frame[0], 
            text="Login",
            bg='red',
            font='30'
            )
        titleWidth = 0.25*windowWidth
        titlex = (windowWidth*0.5) - (titleWidth*0.5)
        title.place(
            width=titleWidth, 
            x=titlex, 
            y=50
            )

        # Enter username
        userTitle = tk.Label(
            self.frame[0], 
            text="Username:", 
            bg='white',
            anchor='w'
            )

        userTitleWidth = 0.1*windowWidth
        userTitlex = (windowWidth*0.5) - (titleWidth*0.5)
        userTitle.place(
            width=userTitleWidth, 
            x=userTitlex, 
            y=75
            )

        userWidth = 0.25*windowWidth
        userx = (windowWidth*0.5) - (titleWidth*0.5)
        user = tk.Entry(self.frame[0])
        user.place(
            width=userWidth, 
            x=userx, 
            y=100
            )

        # Enter password
        passTitle = tk.Label(
            self.frame[0], 
            text="Password:", 
            bg='white',
            anchor='w'
            )

        passTitleWidth = 0.1*windowWidth
        passTitlex = (windowWidth*0.5) - (titleWidth*0.5)
        passTitle.place(
            width=passTitleWidth, 
            x=passTitlex, 
            y=125
            )

        passWidth = 0.25*windowWidth
        passx = (windowWidth*0.5) - (titleWidth*0.5)
        password = tk.Entry(self.frame[0])
        password.place(
            width=passWidth, 
            x=passx, 
            y=150
            )

        # buttons
        butWidth = 0.1*windowWidth
        loginbutton = tk.Button(
            self.frame[0], 
            text='Login', 
            command=lambda: functions.login(
                user,
                password,
                [
                    self.frame[0],
                    self.frame[2],
                    self.frame
                ]
                )
            )
        loginbutton.place(
            width= butWidth,
            x=(windowWidth*0.5) - (titleWidth*0.5), 
            y=175)

        createUserButt = tk.Button(
            self.frame[0], 
            text='Create User', 
            command= lambda: createNewUser(
                self.frame[0], 
                self.frame[1], 
                self.frame)
            )

        createUserButt.place(
            width= butWidth, 
            x=(windowWidth*0.5) - (titleWidth*0.5) + butWidth + 5, 
            y=175
        )