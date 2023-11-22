import os
from tkinter import Tk, Entry, Button
def get_entry_value():
    global value
    value = entry.get() # Получение значения из Entry
    root.destroy()



root = Tk()
entry = Entry(root)
entry.pack()
button = Button(root, text="Введите путь до Папки", command=get_entry_value)
button.pack()
root.mainloop()


print(f"Путь до папки: {value}")

os.chdir(rf"{value}")

formats = {
    "docx": ["doc", "csv", "docx", "pdf", "ppt", "xlsx", "txt", "json", "rtf", "msg"],
    "picture": ["png", "jpg", "gif", "bmp"],
    "archive": ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "lzma"],
    "audio": ["mp3", "aac", "ogg", "wav"],
    "video": ["avi", "mov", "mp4", "mpg", "mpeg", "m4v", "mkv", "wmv", "flv"],
    "certificate": ["pfx", "cer", "p12", "p7b"],
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
                os.replace(fr"{list_files[i]}", rf"{value}]{k}\{list_files[i]}")
        except:
            print("Некоторые файлы могут быть заняты другими программами.")
            continue
print(f"как выглядит папка '{value}' после сортировки: ")
print(*os.listdir(fr"{value}"), sep="\n")
