from constVariables import *
import tkinter as tk
import GUI.homepage as home

class userHome():
    def __init__(self, currentFrame, chosenFrame, frame):
        # initiate the frame
        self.frame = frame
        currentFrame.forget()
        chosenFrame.pack(fill='both', expand=1)
        self.shown()
    
    def shown(self):
        # Title
        title = tk.Label(
            self.frame[2], 
            text="Welcome",
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

        # logout button
        logout = tk.Button(
            self.frame[2],
            text='Logout', 
            command=lambda: home.loginPage(
                self.frame[2], 
                self.frame[0], 
                self.frame
                )
            )
        logout.place(width=150, x=600, y=50)
