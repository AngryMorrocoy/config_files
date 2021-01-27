import socket
from os import environ
from libqtile import widget
from settings.themes import colors

base = lambda fg="text", bg="color1", font="DroidSansMono Nerd Font":{
    "foreground": colors[fg],
    "background": colors[bg],
    "font": font
}

separator = lambda color="color1", padding=5: widget.Sep(**base(fg=color, bg=color), padding=padding)

round_powerline = lambda fg="text", bg="color1": widget.TextBox(
    **base(fg, bg),
    text="",
    fontsize=30,
    padding=0
)

text_icon = lambda fg="text", bg="color1", fontsize=15, text="?", font="DroidSansMono Nerd Font", mouse_callbacks={}: widget.TextBox(
    **base(fg, bg, font),
    fontsize=fontsize,
    text=text,
    padding=1,
    mouse_callbacks=mouse_callbacks
)

groupbox = [
    widget.GroupBox(
        **base(font="Karumbi Bold"),
        fontsize=22,
        padding_x=8,
        padding_y=8,
        margin=3,
        border_width=1,

        highlight_color=colors["color3"],
        active=colors["active"],
        inactive=colors["inactive"],

        highlight_method="line",
        rounded=False,

        disable_drag=True,
        use_mouse_wheel=False,
    ),
    widget.WindowName(
        **base(),
        padding=3,
        fontsize=10
    ),
]

mainbar_widgets = [
    *groupbox,
    round_powerline("color2", "color1"),
    widget.CurrentLayoutIcon(
        **base(bg="color2"),
    ),
    separator("color2", padding=3),
    widget.CurrentLayout(
        **base(bg="color2", font="Dyuthi Regular"),
        fontsize=13
    ),
    separator("color2"),
    round_powerline("color1", "color2"),
    text_icon(fg="color4", bg="color1", text=" "),
    widget.Net(
        **base(bg="color1", font="Dyuthi Regular"),
        interface="wlp1s0",
        fontsize=12
    ),
    separator("color1"),
    round_powerline("color2", "color1"),
    text_icon(fg="color4", bg="color2", text=" "),
    widget.Clock(
        **base(bg="color2", font="agave Nerd Font r"),
        format="%H:%M [%a %d/%m/%Y] ",
        fontsize=14
    ),
]

infobar_widgets = [
    separator("color3"),
    widget.Systray(**base(bg="color3"),
        icon_size=16,
        padding=9
    ),
    separator("color3"),
    round_powerline("color2", "color3"),
    text_icon(bg="color2", fg="color4", text=" ", fontsize=17),
    widget.Memory(**base(bg="color2", font="Dyuthi Regular"),
    ),
    separator("color2", padding=7),
    round_powerline("color3", "color2"),
    text_icon(bg="color3", fg="color4", text=" ", fontsize=17),
    widget.ThermalSensor(**base(bg="color3", font="Dyuthi Regular"), threshold=90, padding=0),
    separator("color3", padding=7),
    widget.Prompt(
        background=colors["color1"],
        padding=10,
        prompt="{}@{}> ".format(socket.gethostname(), environ["USER"]),
        fontsize=12
    ),
    separator("color3", padding=1100)
]


widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
