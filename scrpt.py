import os
import time
os.chdir(r"C:\Users\21004078\Downloads")

formats = {
    "docx": ["doc", "csv", "docx", "pdf", "ppt", "xlsx", "txt", "json", "rtf", "msg"],
    "picture": ["png", "jpg", "gif", "bmp"],
    "archive": ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "lzma"],
    "audio": ["mp3", "aac", "ogg", "wav"],
    "video": ["avi", "mov", "mp4", "mpg", "mpeg", "m4v", "mkv", "wmv", "flv"],
    "certificate": ["pfx", "cer", "p12", "p7b"],
    "other": [],
           }

print("Все папки и файлы:")
print(*os.listdir(), sep="\n")
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
                os.replace(f"{list_files[i]}", rf"C:\Users\21004078\Downloads\{k}\{list_files[i]}")
        except:
            print("Некоторые файлы могут быть заняты другими программами.")
            continue

