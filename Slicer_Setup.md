# Slicer Set up

Setting up the slicer to work with PrintPalette is really simple, firstly I recommand using Orca Slicer. This is becasue of the way it processes, post processing scripts, orignally I was testing with PrusaSlicer but  PrusaSlicer runs these when you save a .gcode file and the issue I had was that this need to be done twice for the script to fully run.

However I swapped to Orca Slicer for another project and when I tested PrintPalette it worked first time excactly how I wanted. I think this is because Orca processes the post processing script when you slice the file, as such at the end of the slicing process, it runs the script without issue.

## Installing Python

To be able to run the PrintPalette script you will need to have Python installed on your compputer (If you use the PrintPalette App, this is not required). I suggest heading to [Python.org](https://www.python.org/) to find the installer for your OS.

## Editing the script

Firstly go to the [Slicer folder](https://github.com/Rushmere3D/PrintPalette/tree/main/Slicer) in the repo and download the .py file you your computer.

The only edit you need to make to the script is changing the wled IP address "wled_ip_address = '###.###.###.###'", I recommend opening the "PrintPalette_Slicer.py" file in [Notepad++](https://notepad-plus-plus.org/).

Then simply edit the IP address with the one from your freshly set up WLED device.

<img width="774" height="50" alt="IP_Address" src="https://github.com/user-attachments/assets/27eacf77-a08f-4b8e-9f11-be6585c03022" />

Now save the file, I recommend the python/scripts folder to make the next step easier.

We can now add it to Orca Slicer

## Orca Slicer set up

To use the post processing script, you need to have the full file path of both Python and the script on my computer these would be C:\Python312\python.exe and C:\Python312\Scripts\printpalette_slicer.py.

You then place both these file paths in the Post-Processing Scripts box found under the "Others" tab of the printer settings

<img width="479" height="374" alt="Orca_PP" src="https://github.com/user-attachments/assets/bf125251-c450-426e-8da6-a4dbe42d20c8" />

## Filament colours

Now that the script is ready to go, you filament set up is next.

So an interesting thing here is that the colour we can easly change in Orca by clicking the numbered coloured box, is in fact the Extruder (tool) colour and not the filament colour (as far as the slicer is concerned) and this is the data the script captures.

It's important to only have the number of colours displayed that your LED segments are set up for, otherwise it will overwrite the last "Tool" segment on the LEDs.

So here is my Bambu Lab P1S with single AMS for example.

<img width="479" height="127" alt="Orca_Filaments" src="https://github.com/user-attachments/assets/ff50fb4f-d4f5-4179-8185-13add2815d6a" />

## Results

So with all this done and assuming you have the LEDs connected to your WLED device and it is powered up, slicing a file will result in the "filament" colours being sent to the WLED device and displayed on the LED stip.

https://github.com/user-attachments/assets/7696560f-d18c-44b6-b875-31b5234a0a1f


Changing a colour or other parameter in Orca resuting in needing to slicer again and will clear the LEDs and send the new colours.

# Acknowledgments

Big thanks to my friend Richard for his help with the first PrintPalette script, Although I knew what and how I wanted it to work I didn't know how to put this all together. Thanks
