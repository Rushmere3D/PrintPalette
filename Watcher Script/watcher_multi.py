import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# Map folders to printer info
WATCH_CONFIG = {
    r"D:\VoronGcode": "192.168.1.221",  # Voron printer WLED IP
    r"D:\ToolchangerGcode": "192.168.1.204",  # Toolchanger printer WLED IP
    r"D:\TestGcode": "192.168.1.215",  # Test printer WLED IP
}

# Path to your shared LED script
LED_SCRIPT = r"C:\Python312\Scripts\printpalette_slicer_multi.py"

class MultiFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".gcode"):
            # Match folder → IP
            for folder, ip in WATCH_CONFIG.items():
                if event.src_path.startswith(folder):
                    print(f"New G-code detected in {folder}: {event.src_path}")
                    env = os.environ.copy()
                    env["SLIC3R_PP_OUTPUT_NAME"] = event.src_path
                    env["WLED_IP_ADDRESS"] = ip  # pass printer IP
                    subprocess.Popen(["python", LED_SCRIPT], env=env)
                    break

if __name__ == "__main__":
    observers = []
    for folder in WATCH_CONFIG.keys():
        event_handler = MultiFolderHandler()
        observer = Observer()
        observer.schedule(event_handler, folder, recursive=False)
        observer.start()
        observers.append(observer)
        print(f"Watching folder: {folder}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for observer in observers:
            observer.stop()
        for observer in observers:
            observer.join()
