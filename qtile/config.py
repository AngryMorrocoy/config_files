from libqtile import bar, hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import mainbar_widgets, infobar_widgets, widget_defaults, extension_defaults
from settings.mouse import mouse
import settings.hooks

from libqtile.config import Screen

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

