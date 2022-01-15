#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:14:33 2022

@author: clockshield
"""


from tkinter import *
import random
from PIL import ImageTk, Image
root=Tk()
root.title("lol")


a = 20
b = 20
try:
    print(a)
    print(b)
    print(somevariable)
except NameError:
    print("THIS IS A NAME ERROR LOL GET NOOB")
    
try:
    root.geometry("200")
except:
    print("lol ur dumb how u get this error lololol")
    
try:
    numbr = 420
    print("OMG THE NUNMBER IS " + numbr)
except TypeError:
    print("YOU GOT TYPE ERROR USE POKEBALL TO CATCH")
root.mainloop()