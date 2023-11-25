import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser


def callback(url):
    webbrowser.open_new(url)

first = tk.Tk()
c = tk.Canvas(first, width=500, height=500)
img = ImageTk.PhotoImage(Image.open("D:\Projects\project_sort\welcome.png"))


c.create_image(0, 0, image=img, anchor="nw")
b = tk.Label(text="", anchor="sw")
c.pack()
b.pack()
link1 = Label(first, text="visit my github", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://github.com/artnovak"))

first.mainloop()
