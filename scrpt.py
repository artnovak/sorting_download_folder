import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, Entry, Button

def clicked():
    messagebox.showinfo('Заголовок', 'Текст')

def choose_dir():
    global input_value
    input_value = filedialog.askdirectory()

window = tk.Tk()
window.title("PythonExamples.org")
window.geometry("600x300")

button = Button(
    window,
    text="fill up absolute path for download folder",
    command=choose_dir,
    width=40,
    height=3)
button.pack()


# Run the application
window.mainloop()
