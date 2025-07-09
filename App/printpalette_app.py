import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
CREATE_NO_WINDOW = 0x08000000  # Windows-specific flag to hide CMD windows
import re
import ipaddress
import os


CONFIG_FILE = "config.txt"

# Themes
LIGHT_THEME = {
    "bg": "#f0f0f0",
    "fg": "#000000",
    "entry_bg": "#ffffff",
    "btn_bg": "#e0e0e0",
    "btn_fg": "#000000"
}

DARK_THEME = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "entry_bg": "#2e2e2e",
    "btn_bg": "#444444",
    "btn_fg": "#ffffff"
}

current_theme = LIGHT_THEME

def save_config(ip, theme_name):
    with open(CONFIG_FILE, "w") as f:
        f.write(f"ip={ip}\n")
        f.write(f"theme={theme_name}\n")

def load_config():
    ip = "192.168.1.100"
    theme_name = "light"
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            for line in f:
                if line.startswith("ip="):
                    ip = line.split("=", 1)[1].strip()
                elif line.startswith("theme="):
                    theme_name = line.split("=", 1)[1].strip()
    return ip, theme_name

def apply_theme():
    theme = current_theme
    root.configure(bg=theme["bg"])
    top_frame.configure(bg=theme["bg"])  # Ensure top frame matches

    for widget in root.winfo_children():
        try:
            widget.configure(bg=theme["bg"], fg=theme["fg"], highlightbackground=theme["bg"])
            if isinstance(widget, tk.Button):
                widget.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=theme["entry_bg"], fg=theme["fg"])
        except:
            pass

    for widget in top_frame.winfo_children():
        try:
            widget.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])
        except:
            pass

    color_frame.configure(bg=theme["bg"])

def update_theme_icon():
    if current_theme == DARK_THEME:
        theme_button.config(text="🌞")  # Light mode icon
    else:
        theme_button.config(text="🌙")  # Dark mode icon

def toggle_theme():
    global current_theme
    current_theme = LIGHT_THEME if current_theme == DARK_THEME else DARK_THEME
    apply_theme()
    update_theme_icon()
    save_config(ip_entry.get(), "dark" if current_theme == DARK_THEME else "light")

def send_curl_command(url):
    print(f"Sending: {url}")
    try:
        subprocess.run(["curl", url], check=True, creationflags=CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        print(f"Failed request: {e}")
        messagebox.showerror("Error", f"Failed to send command to WLED.\n{url}")

def send_color_to_wled(hex_color, wled_ip, ss_value):
    color = hex_color.lstrip('#')
    url = f"http://{wled_ip}/win&T=1&A=64&FX=0&SX=0&SS={ss_value}&CL=H{color}"
    send_curl_command(url)

def clear_wled_slots(wled_ip):
    curl_command = f'curl "http://{wled_ip}/win&PL=1"'
    subprocess.run(curl_command, creationflags=CREATE_NO_WINDOW)

def display_color_blocks(color_list):
    for widget in color_frame.winfo_children():
        widget.destroy()
    for hex_color in color_list:
        tk.Label(color_frame, bg=hex_color, width=4, height=2, relief='ridge', bd=1).pack(side=tk.LEFT, padx=3)

def manual_clear_leds():
    wled_ip = ip_entry.get().strip()
    

    try:
        ipaddress.ip_address(wled_ip)
    except ValueError:
        messagebox.showerror("Invalid IP", "Please enter a valid IP address.")
        return

    # Clear LEDs using WLED preset before sending new colors
    clear_wled_slots(wled_ip)

    
    # Clear the GUI color boxes
    for widget in color_frame.winfo_children():
        widget.destroy()

    messagebox.showinfo("Done", f"Cleared LED slots.")


def open_gcode_file():
    wled_ip = ip_entry.get().strip()

    try:
        ipaddress.ip_address(wled_ip)
    except ValueError:
        messagebox.showerror("Invalid IP", "Please enter a valid IP address.")
        return


    theme_name = "dark" if current_theme == DARK_THEME else "light"
    save_config(wled_ip, theme_name)

    filepath = filedialog.askopenfilename(filetypes=[("GCode Files", "*.gcode")])
    if not filepath:
        return

    print(f"Opening file: {filepath}")
    colors_to_send = []

    try:
        with open(filepath, 'r') as file:
            for line in file:
                if "extruder_colour" in line.lower():
                    matches = re.findall(r"#([A-Fa-f0-9]{6})", line)
                    for match in matches:
                        colors_to_send.append(f"#{match}")

        if not colors_to_send:
            messagebox.showwarning("Not Found", "No 'extruder_colour' colors found.")
            return

        # Clear LEDs using WLED preset before sending new colors
        clear_wled_slots(wled_ip)

        progress["value"] = 0
        status_label.config(text="Sending...")
        root.update_idletasks()

        for index, hex_color in enumerate(colors_to_send):
            send_color_to_wled(hex_color, wled_ip, index)
            progress["value"] = ((index + 1) / len(colors_to_send)) * 100
            root.update_idletasks()

            progress["value"] = 0
            status_label.config(text="Done!")


        display_color_blocks(colors_to_send)
        messagebox.showinfo("Done", f"Sent {len(colors_to_send)} colors.")

    except Exception as e:
        print(f"Exception: {e}")
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Print Palette")
root.geometry("600x350")

# Load config
saved_ip, saved_theme = load_config()
current_theme = DARK_THEME if saved_theme == "dark" else LIGHT_THEME

# Top frame for header and theme button
top_frame = tk.Frame(root)
top_frame.pack(fill="x", pady=(5, 0), padx=5)

theme_button = tk.Button(top_frame, text="", command=toggle_theme, bd=0, font=("Arial", 14))
theme_button.pack(side="right", padx=5)
update_theme_icon()

# Main content
tk.Label(root, text="WLED IP Address:").pack(pady=(10, 0))
ip_entry = tk.Entry(root, width=30)
ip_entry.insert(0, saved_ip)
ip_entry.pack(pady=5)

tk.Button(root, text="Clear LED Slots", command=manual_clear_leds).pack(pady=15)

tk.Button(root, text="Select GCode File", command=open_gcode_file).pack(pady=15)

tk.Label(root, text="Colors Sent:").pack(pady=(10, 0))
color_frame = tk.Frame(root)
color_frame.pack(pady=10)

progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

apply_theme()
root.mainloop()

