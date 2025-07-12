# PrintPalette

<img width="512" height="512" alt="PrintPaletteLogo" src="https://github.com/user-attachments/assets/be7c37ad-a735-47a8-87ea-685d6eb9c67c" />


The simple filament colour indicator for multi-tool 3D printers, 3D printer add-ons such as the Prusa MMU, Bambu Lab AMS, community add-ons like the ERCF, Box Turtle and others.

Not limited by printer or add-on firmware and only requires a WLED device and RGB LEDs. Although additional functions can be used when connected to a Moonraker enabled printer.

Print Palette can work in two ways, via a post processing script directly in the slicer (Orca preferred) or via a standalone windows app. Print Palette then sends commands to a device running WLED such as an [WeMos D1 Mini ESP8266](https://s.click.aliexpress.com/e/_oBwEcnE) with a [strip of RGB LEDs](https://s.click.aliexpress.com/e/_ooGWccU) attached to display the filament colour that needs to be loaded into its corresponding tool.


# Getting Started


The first thing you need to do, to use PrintPalette is to set up your WLED device. I use a simple D1 Mini from AliExpress which is less than £2, [WeMos D1 Mini](https://s.click.aliexpress.com/e/_oBwEcnE) .

Getting WLED on the device is simple and I suggest using the WLED web installer by following “Flashing method 1” from [WLED website](https://kno.wled.ge/basics/install-binary/).

Once you’ve completed this you’ll be able to connect to the device running WLED though the Web UI and be presented with this screen. (Screenshot)

Now we need to tell WLED a few things, 1) How many LEDs you are using 2) How many tools you are using. 3) Set up a default preset.

## LED Length (Count)

So the number of LEDs you use can be set in “Config - LED Preferences”. This is the total number of LEDs you will be using, this doesn’t have to match the tools you will be using for example I use an 8 LED PCB strip for a 4 tool printer allowing 2 LEDs for each tool.

<img width="389" height="467" alt="LED_Length" src="https://github.com/user-attachments/assets/fc928c1f-5409-4612-85c2-cddbbd8ea47b" />

Once you’ve entered the number of LEDs, click “Save” and then Back to return to the homescreen.

## “Tool” set up

To set up the “Tools” we will use a feature of WLED called “[Segments](https://kno.wled.ge/features/segments/)”, this basically allows us to set the LED strip into segments where each segment corresponds to a “tool” in the 3D printer or add-on.

To set up a segment, first click the segment name and call it something referencing the tool number I simply use T0, T1, T2 etc.

Next we want to set the Start and End LED numbers, this refers to the physical LED number on the strip, so for my example of an 8 LED strip for 4 tools I would be 0-2, 2-4, 4-6 and 6-8. Create the require segments for your set up.

<img width="331" height="364" alt="Seg_0" src="https://github.com/user-attachments/assets/e7fd227c-9425-4be7-a9fc-e5605537ba79" /> <img width="318" height="324" alt="Seg_1" src="https://github.com/user-attachments/assets/1e089dbd-6081-4836-8c7c-ca582d5772df" /> <img width="326" height="328" alt="Seg_2" src="https://github.com/user-attachments/assets/da1266c4-c009-4943-a563-72ec93bcb296" /> <img width="329" height="327" alt="Seg_3" src="https://github.com/user-attachments/assets/ca574d57-4ee0-4d5a-90a9-a55cc70e5039" />

## Default Preset

Now we have set our LED count and tool segments, we want to save this as a preset, this needs to be set up so that the LEDs are off and in slot “1”. This will be how we clear the LEDs later.

So first select each segment one at a time and ensure they are set to off.

Now click + preset button, give this a name such OFF, RESET or CLEAR and ensure the tick box for "Use curent state”, "save segment bounds" are ticked and tick the box "Apply at boot", lastly ensure "Save to ID" is set to 1.

Click save.

<img width="311" height="397" alt="Preset" src="https://github.com/user-attachments/assets/af422d3f-d5c9-45b1-bf91-9366ba54e307" />

## Thats WLED set up.
