from libqtile import bar, hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import mainbar_widgets, infobar_widgets, widget_defaults, extension_defaults
from settings.mouse import mouse
from settings.path import qtile_path

from libqtile.config import Screen

import subprocess
from os import path


screens = [
    Screen(
        top=bar.Bar(
            mainbar_widgets, 17
        ),
        bottom=bar.Bar(
            infobar_widgets, 20
        )
    ),
]

@hook.subscribe.startup_once
def load_external_conf():
    # Called once per start, extra configuration
    script_file = path.join(qtile_path, "load_xinput.py")
    config_file = path.join(qtile_path, "xinput_props.json")

    subprocess.call([ script_file, config_file])
    subprocess.call(path.join(qtile_path, "autostart.sh"))


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []

wmname = "LG3D"

