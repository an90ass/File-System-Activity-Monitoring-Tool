import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ctypes
from datetime import datetime
import os
import requests

deleted_files = {}
recently_created = set()

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_event(message):
    log_file_path = r""  # specify your path
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

def created(event):
    # Check if the file was recently deleted (potential move)
    for deleted_file, deleted_time in deleted_files.items():
        if os.path.basename(deleted_file) == os.path.basename(event.src_path):
            message = f"File moved: {deleted_file} -> {event.src_path} ----- Time: {get_current_time()}"
            print(message)
            showMessage(message)
            log_event(message)
            del deleted_files[deleted_file]
            return

    # Otherwise, treat it as a normal file creation
    message = f"File created: {event.src_path} ----- Time: {get_current_time()}"
    print(message)
    showMessage(message)
    log_event(message)

    if os.path.isdir(event.src_path):
        recently_created.add(event.src_path)

def deleted(event):
    deleted_files[event.src_path] = time.time()
    message = f"File deleted: {event.src_path} ----- Time: {get_current_time()}"
    print(message)
    showMessage(message)
    log_event(message)

def modified(event):
    if event.src_path in recently_created:
        recently_created.remove(event.src_path)
        return

    message = f"File modified: {event.src_path} ----- Time: {get_current_time()}"
    print(message)
    showMessage(message)
    log_event(message)

def moved(event):
    src_dir = os.path.dirname(event.src_path)
    dest_dir = os.path.dirname(event.dest_path)

    if src_dir == dest_dir:
        message = f"File renamed: {event.src_path} -> {event.dest_path} ----- Time: {get_current_time()}"
    else:
        message = f"File moved: {event.src_path} -> {event.dest_path} ----- Time: {get_current_time()}"

    print(message)
    showMessage(message)
    log_event(message)

def showMessage(message):
    title = "Security Alert"
    ID = 0  # specify your ID
    TK = ''  # specify your token
    send = f"https://api.telegram.org/bot{TK}/sendMessage?chat_id={ID}"
    tele = f"{send}&text=\ud83d\udd12 *{title}* \ud83d\udd12\n\n" \
           f"\u26a0\ufe0f *Event:*  {message}\n" \
           f"\ud83d\uddd3 *Event Time:* {get_current_time()}"
    requests.get(tele)
    # ctypes.windll.user32.MessageBoxW(None, message, title, 0)

if __name__ == "__main__":
    path = ""  # specify your path
    evo = FileSystemEventHandler()
    evo.on_created = created
    evo.on_deleted = deleted
    evo.on_modified = modified
    evo.on_moved = moved

    observer = Observer()
    observer.schedule(evo, path, recursive=True)
    observer.start()
    try:
        while True:
            current_time = time.time()
            for deleted_file in list(deleted_files):
                if current_time - deleted_files[deleted_file] > 5:
                    del deleted_files[deleted_file]
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
