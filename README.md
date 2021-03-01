# AngryMorrocoy's (Manuel Rivas) configuration files

##### Config list

- Gtk-3.0
- Openbox
- Qtile
- Rofi
- Termite
- Vifm
- Vim [submodule](https://github.com/AngryMorrocoy/MyVim)
- X11
- Zsh
---

### Gtk-3.0


- **`bookmakrs`**

    Nothing to resalt here, just some bookmarks for gui file managers.

- **`gtk.css`**

    Just one style, for adding a 2px padding to termite.

- **`settings.ini`**

    Standard settings, for the theme and the font type.

---

### Openbox

I don't really use too much openbox, I like more qtile but here is a small explanation of what this files do.<br>

- **`autostart`**

    When first load, charge some stuff like:
    - ***cbatticon*** (For the battery icon)
    - ***volumeicon*** (Volume icon)
    - ***nm-applet*** (Network connections icon)
    - ***picom*** (A compositor, for transparency)
    - ***nitrogen*** (Wallpaper reload)
    - ***xfce4-panel*** (The panel/bar, of xfce4)

- **`environment`**

    It does not do nothing yet.

- **`menu.xml`**

    The configuration for the menu, when right click on the desktop.

- **`rc.xml`**

    Here is where the magic happens, all the configuration for openbox, keybindings and all of that resides in this file.
---

### Qtile

My favorite window manager, for the moment at least. The configuration is modularized. More info about what happens there, you can read the files, are (I think) whell documented.

##### settings
- **`extra.py`**

    This file contain extra functions (utilities), that I use in one of the bars.
- **`groups.py`**

    Not too much this file is the encharged of the groups, I use 8 of them.
- **`keys.py`**

    One of the most important, in this file resides all the keybindings that I use.
- **`layouts.py`**

    Configuration for the layouts, like the padding and that stuff.
- **`mouse.py`**

    Configuration for the mouse, how it should "work".
- **`path.py`**

    Only defines a variable, a path variable equivalent to *$HOME/.config/qtile*.

- **`themes.py`**

    This file doesn't define the themes that I use, instead it have functions that loads any of the files I parse to it, changing almost all the margins and bar colors.
- **`widgets.py`**

    One of the most extensive, It defines all the widgets and combination of them, that will appear on the bars, those are loaded on the `config.py` file at the root of the qtile directory.

#### themes

On this file are json files, that contains some color combinations, those are readed by the `themes.py` script and used almost everywhere on the configuration for multiple stuff. Current themes are:

- Default
- Artistic
- Rose-purple
- Sepiangel

#### Root

- **`autostart.sh`**

    This script, called once loads some common programs, those are:
    - ***cbatticon*** (For the icon battery on the systray).
    - ***volumeicon*** (For the volume icon on the systray).
    - ***nm-applet*** (For the wifi icon on the systray).
    - ***redshift-gtk*** (Starts by default redshift, caring my eyes (?)).
    - ***picom*** (Compositor, for transparency).
    - ***nitrogen*** (For the wallpapers, this line reloads it).

- **`load_xinput.py`**

    Script that loads some xinput properties from `xinput_props.json` at startup, for the laptop pad.

- **`xinput_props.json`**

    Json file with xinput properties readed by the `load_xinput.py` script.

- **`config.py`**

    The most important file, this file is the one readed by qtile when starting, here is where the setup of the screen happens, the bars are loaded, and everything happens.

---

### Vifm

#### colors
    Here resides the colorschemes for the Vi file manager.
    - Default (The default colorscheme for vifm)
    - gruvbox (Gruvbox colorscheme for vifm)

