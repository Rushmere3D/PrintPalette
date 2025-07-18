# PrintPalette

<img width="512" height="512" alt="PrintPaletteLogo" src="https://github.com/user-attachments/assets/be7c37ad-a735-47a8-87ea-685d6eb9c67c" />

The purpose of PrintPalette was to provide a simple filament colour indicator for multi-tool 3D printers, 3D printer add-ons such as the Prusa MMU, Bambu Lab AMS, community add-ons like the ERCF, Box Turtle and others.

The intention is that, if you don't preload your printer or add-on before painting and slicing your chosen model, then using PrintPalette will aid in identifying which colour filament needs to be loaded in a specific tool/lane/channel etc

It is not limited by printer or add-on firmware and only requires a WLED device and RGB LEDs. Although additional functions can be used when connected to a Moonraker enabled printer (more information coming soon).

PrintPalette can work in two ways, via a post processing script directly in the slicer (Orca preferred) or via a standalone windows app. PrintPalette then sends commands to a device running WLED such as an [WeMos D1 Mini ESP8266](https://s.click.aliexpress.com/e/_oBwEcnE) with a [strip of RGB LEDs](https://s.click.aliexpress.com/e/_ooGWccU) attached to display the filament colour that needs to be loaded into its corresponding tool.


# Getting Started

Setting up PrintPalette consists of the WLED setup, Slicer setup and/or App setup. Follow the guides below to set each step up.

## [WLED Set up](https://github.com/Rushmere3D/PrintPalette/blob/main/WLED_Setup.md#wled-set-up)

## [Slicer Set up](https://github.com/Rushmere3D/PrintPalette/blob/main/Slicer_Setup.md#slicer-set-up)

## [App Set up](https://github.com/Rushmere3D/PrintPalette/blob/main/App_Setup.md#app-set-up)

# STLs?

I have deliberately not included any 3D print files because everyone will likely want to mount the LEDs differently. I am working on some of my own mounts and will upload them once fully tested.

However please feel free to create mounts and upload them to your chosen 3D print file repo and I will happily include links here.
