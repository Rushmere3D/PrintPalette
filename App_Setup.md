# App Set up

I created the PrintPalette App because it occurred to me that some people may 1) not want to use a post processing script in Orca Slicer or 2) maybe they didn't use Orca Slicer but another slicer or 3) they had .gcode files they had already painted in the slicer and didn't want to do this again.

The App is a ready to go .exe with a config file for remebering the WLED device IP and app theme (Yes it have a light/dark theme select :-p)

## How to use

First simply download the PrintPalette_App.exe and Config.txt file from the [App folder](https://github.com/Rushmere3D/PrintPalette/tree/main/App)

Opening the app with show this screen

<img width="602" height="382" alt="App_First" src="https://github.com/user-attachments/assets/28316a69-30ac-4178-89dd-58c1350ac12b" />

First thing to do it set your WLED IP address, this is the IP address you use to access the WLED device you set up earlier.

You can also change the theme to dark if you wish using the icon in the top right.

The interface is simple and only have 2 buttons, "Clear LED Slots" does exactly that and is just a manual clear option if needed.

The next button is the important one "Select GCode File", clicking this will open a file browser allowing you to select a .gcode file you have pre painted for multi colour printing.

Once you click open in the file browser, the PrintPalette App will automatically extract the "filament" colours and send them to the LEDs. It will first clear the LEDs and then send what it's taken from the selected .gcode file. It's pretty quick so although I've included a progress bar the app will quickly display a confirmation box and you will see the colours just send to the LEDs are also displayed in the app for confirmation.

https://github.com/user-attachments/assets/0924a035-e0ee-4742-bf9a-9e65bba83c94

Closing the app will update the Config.txt with the IP address and theme choice ready for next time you open it.

And that's it, simple. 
