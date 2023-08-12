import ttkbootstrap
import ttkbootstrap.constants
import tkinter as tk
from tkinter import Messagebox as msgbox
import sys

class pri():
  def __init__(self):
    self = ttkbootstrap.Window()

  def msgbox(self,choice,title,text):
    if choice == 1:
      msgbox.showinfo(title,text)
    elif choice == 2:
      msgbox.showwarning(title,text)
    elif choice ==3:
      msgbox.showerror(title,text)

  def EXIT(self):
    sys.exit()
