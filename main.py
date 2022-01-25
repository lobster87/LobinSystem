"""This is a graduate management softwhere"""
import tkinter as tk
from GUI.homepage import loginPage
from constVariables import *
""" Create Window """
window = tk.Tk()
window.title('Graduate management platform')
window.geometry(f'{windowWidth}x{windowHeight}')
window.resizable(False, False)

"""
Set up frames in list

0 - login
1 - create user
2 - user homepage
"""
frames = [
    tk.Frame(window, bg='white'), 
    tk.Frame(window, bg='white'),
    tk.Frame(window, bg='white')
    ]

loginPage(frames[0], frames[0], frames)
window.mainloop()