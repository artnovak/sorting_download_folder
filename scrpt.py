import os
from tkinter import Tk, Entry, Button, filedialog, ttk, messagebox
import time

def choose_directory():
    messagebox.showinfo('info', 'Choose the directory where you want to sort files')
    global input_value
    input_value = filedialog.askdirectory()

def quitWin():
    res = messagebox.askyesno('Оля ты чиво', 'are you sure about that?')
    if res == True:
        messagebox.showinfo('info', '1 ... 2 ... 3')
        time.sleep(3)
        quit()
    elif res == False:
        pass
    else:
        messagebox.showerror('error', 'something went wrong!')
try:
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text='Choose the directory where you want to sort files').grid(row=0, column=0, sticky="W")
    ttk.Label(frm, text='').grid(row=1)
    ttk.Button(frm, text="Quit", command=quitWin).grid(row=2, column=2)
    ttk.Button(frm,
        text="choose directory",
        command=choose_directory).grid(row=2, column=3)
    root.mainloop()
    print(f"Путь до папки: {input_value}")
    os.chdir(rf"{input_value}")
except:
    print("something went wrong")
    quit()
formats = {
    "docx": ["doc", "csv", "docx", "pdf", "ppt", "xlsx", "txt", "json", "rtf", "msg"],
    "picture": ["png", "jpg", "gif", "bmp", "PNG", "GIF", "JPEG", "jpeg", "JPG", "HEIC"],
    "archive": ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "lzma"],
    "audio": ["mp3", "aac", "ogg", "wav"],
    "video": ["avi", "mov", "mp4", "mpg", "mpeg", "m4v", "mkv", "wmv", "flv", "MOV"],
    "certificate": ["pfx", "cer", "p12", "p7b"],
    "torrent": ["torrent"],
    "config": ["conf", "msi", "py"],
    "other": [],
           }
list_files = os.listdir()
set_files = set()
for k, v in formats.items():
        try:
            os.mkdir(f"{k}")
        except:
            continue
for i in range(len(list_files)):
    try:
        format_file = list_files[i][::-1][:list_files[i][::-1].index(".")]
    except:
        continue
    format_file = format_file[::-1]
    set_files.add(format_file)
    for k, v in formats.items():
        try:
            if format_file in v:
                os.replace(fr"{list_files[i]}", rf"{input_value}\{k}\{list_files[i]}")
        except:
            print("Некоторые файлы могут быть заняты другими программами.")
            continue
other = os.listdir()
for i in range(len(other)):
     if not os.path.isdir(other[i]):
         os.replace(fr"{other[i]}", rf"{input_value}\other\{other[i]}")

print(f"как выглядит папка '{input_value}' после сортировки: ")
print(*os.listdir(fr"{input_value}"), sep="\n")
