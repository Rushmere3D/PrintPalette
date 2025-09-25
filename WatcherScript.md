This contains info on creating the watcher script for PrintPalette. (Work In Progess)

# Watcher Script Set up

## Multi-Printer G-code Watcher with Auto-Running .exe

This will let you:

- Watch multiple folders where OrcaSlicer saves .gcode.
- Run one LED script but with different WLED IP addresses depending on the folder.
- Package the watcher as a .exe that starts automatically with Windows.

### 1. Install Requirements

1 Install Python 3 (already done in your case).

2 Open PowerShell and install the watchdog library:

```
pip install watchdog
```

3 Install pyinstaller for building .exe files:

```
pip install pyinstaller
```

### 2. Create the Watcher Script

1 Open Notepad (or VS Code).

2 Paste this script and save it as watcher.py or use the pre-uploaded file:

```
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# Map folders to printer WLED IPs (edit these!)
WATCH_CONFIG = {
    r"C:\VoronGcode": "192.168.1.50",
    r"C:\BambuGcode": "192.168.1.60",
    r"C:\PrusaGcode": "192.168.1.70",
}

# Path to your shared LED script
LED_SCRIPT = r"C:\Python312\Scripts\printpalette_slicer.py"

class MultiFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".gcode"):
            for folder, ip in WATCH_CONFIG.items():
                if event.src_path.startswith(folder):
                    print(f"New G-code detected in {folder}: {event.src_path}")
                    env = os.environ.copy()
                    env["SLIC3R_PP_OUTPUT_NAME"] = event.src_path
                    env["WLED_IP_ADDRESS"] = ip
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
```

3 Edit the WATCH_CONFIG/LED_SCRIPT sections:

- Replace the folder paths with the actual paths where you export G-code for each printer and the LED script.
- Replace the IPs with the correct WLED IPs for each printer.

4 Save the file.

### 3. Update Your LED Script

In printpalette_slicer.py, change the WLED IP definition at the top:

```
import os
wled_ip_address = os.environ.get("WLED_IP_ADDRESS", "192.168.1.215")
```

This way, the watcher decides which IP to use.

### 4. Test the Watcher in Python

In PowerShell, run:

```
python watcher.py
```

- You should see:
Watching folder: C:\Users\James\Documents\VoronGcode etc.

- Export a G-code into one of those folders → it should detect it and run the LED script with the correct IP.

If it works, move to the next step.

### 5. Build the .exe

1 In PowerShell, navigate to the folder where watcher.py is saved:

```
cd C:\path\to\watcher\folder
```

2 Run PyInstaller:

```
pyinstaller --onefile --noconsole watcher.py
```

3 After it finishes, you’ll find watcher.exe in the new dist folder.

### 6. Auto-Start the Watcher

1 Press Win + R, type:

```
shell:startup
```

→ Opens your Startup folder.

2 Copy watcher.exe from dist into this folder.

3 Restart your computer → the watcher will now always run in the background at login.

### Done! You now have a background .exe that watches multiple folders, launches one LED script, and passes the correct WLED IP based on which printer’s G-code you saved.
