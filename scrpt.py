import os
from tkinter import Tk, Entry, Button
def get_entry_value():
    global value
    value = entry.get() # Получение значения из Entry
    root.destroy()

def change():
    button['text'] = "fill up absolute path for download folder"

root = Tk()
entry = Entry(root, width=50)
entry.pack()
button = Button(
    root,
    text="fill up absolute path for download folder",
    command=get_entry_value,
    width=40,
    height=3)
button.config(command=change())
button.pack()
root.mainloop()


print(f"Путь до папки: {value}")

os.chdir(rf"{value}")

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
                os.replace(fr"{list_files[i]}", rf"{value}\{k}\{list_files[i]}")
        except:
            print("Некоторые файлы могут быть заняты другими программами.")
            continue

other = os.listdir()
for i in range(len(other)):
     if not os.path.isdir(other[i]):
         os.replace(fr"{other[i]}", rf"{value}\other\{other[i]}")

print(f"как выглядит папка '{value}' после сортировки: ")
print(*os.listdir(fr"{value}"), sep="\n")
