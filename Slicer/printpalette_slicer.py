import os
import re
import subprocess
CREATE_NO_WINDOW = 0x08000000  # Windows-specific flag to hide CMD windows
import time
# User-configurable variables
wled_ip_address = '192.168.1.204'  # Set your WLED IP address here

# Function to send a curl command to WLED
def send_curl_to_wled(ss_value, color):
    curl_command = f'curl "http://{wled_ip_address}/win&T=1&A=64&FX=0&SX=0&SS={ss_value}&CL=H{color}"'
    subprocess.run(curl_command, shell=True, creationflags=CREATE_NO_WINDOW)

# Function to clear LEDs using WLED preset
def clear_leds_with_preset():
    curl_command = f'curl "http://{wled_ip_address}/win&PL=1"'
    subprocess.run(curl_command, shell=True, creationflags=CREATE_NO_WINDOW)


# Retrieve the output file name from the environment variable
env_slicer_pp_output_name = os.getenv('SLIC3R_PP_OUTPUT_NAME')

if env_slicer_pp_output_name:
    try:
        with open(env_slicer_pp_output_name, 'r') as file:
            for line in file:
                if line.startswith('; extruder_colour ='):
                    # Extract color codes from the line
                    colors = re.findall('#([0-9A-Fa-f]{6})', line)
                    
                    # Clear LEDs first
                    clear_leds_with_preset()
                    
                    for index, color in enumerate(colors):
                        # Send color to WLED with incrementing SS value
                        send_curl_to_wled(index, color)
                    break  # Stop reading the file after finding the extruder_colour line
                    time.sleep(0.1)
    except FileNotFoundError:
        print(f"File {env_slicer_pp_output_name} not found.")
else:
    print("SLIC3R_PP_OUTPUT_NAME environment variable is not set.")