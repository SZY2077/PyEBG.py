import ttkbootstrap
import ttkbootstrap.constants
import tkinter as tk
from tkinter import Messagebox as msgbox
import sys

class pri():
  def __init__(self,theme,x,y):
    self = ttkbootstrap.Window(themename=theme)
    self.geometry(str(str(x)+"x"+str(y))

  def msgbox(self,choice,title,text):
    if choice == 1:
      msgbox.showinfo(title,text)
    elif choice == 2:
      msgbox.showwarning(title,text)
    elif choice ==3:
      msgbox.showerror(title,text)

  def EXIT(self):
    sys.exit()
