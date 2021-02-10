from libqtile import widget
from settings.themes import colors
from bs4 import BeautifulSoup
from os import environ
import subprocess
import requests
import re

def get_dollar():
    monitordollar_url = "https://monitordolarvzla.com/category/promedio-del-dolar/"
    try:
        page = requests.get(monitordollar_url)
    except Exception as e:
        return re.search("<class '(.*)'", str(e.__class__)).groups()[0]
    if not page.ok:
        return "Couldn't get the data"

    soup = BeautifulSoup(page.content, "lxml")

    dollar_paragraph = ""

    for tag in filter(lambda tag: tag.has_attr("class"), soup.find_all("div")):
        if "entry-content" in tag.attrs["class"]:
            dollar_paragraph = tag.p.text
            break
    extract_pattern = "(\d+(?:/\d+){2}) (\d+:\d+ (?:AM|PM)) Bs ([^\s]+)"

    date, time, dollar_price = re.search(extract_pattern, dollar_paragraph).groups()

    return f"{dollar_price} Bs (Last update: [{date}] at {time})"


def get_battery_status():
    ICONS = {
        "C": [x+" " for x in ""],
        "D": [x+"  " for x in ""],
    }
    try:
        bats_out = subprocess.check_output("bats", universal_newlines=True).rstrip()
    except subprocess.CalledProcessError:
        return "..."

    batt_lvl, batt_status = re.search("^(\d+)(\D{1})$", bats_out).groups()
    batt_lvl = int(batt_lvl)

    if batt_status == "F":
        return f"  {batt_lvl}%"

    batt_icon = ""

    for i, icon in enumerate(ICONS[batt_status], 1):
        if round(batt_lvl/10) <= i:
            break
        batt_icon = icon
    return f"{batt_icon}{batt_lvl}%"

# print(get_battery_status())

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
        this_current_screen_border=colors["color3"],
        inactive=colors["inactive"],

        highlight_method="line",
        rounded=False,

        disable_drag=True,
        use_mouse_wheel=False,
    ),
    widget.WindowName(
        **base(font="JetBrains Mono Medium Nerd Font"),
        padding=3,
        fontsize=10
    ),
]

mainbar_widgets = [
    widget.Prompt(**base(bg="color1", font="agave regular Nerd Font Complete"),
        prompt=f" {environ['USER']}> ",
        padding=5
    ),
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
    round_powerline("color1", "color2"),
    widget.GenPollText(**base(bg="color1", font="mononoki-Regular Nerd Font complete"), fontsize=15,
                       func=get_battery_status, update_interval=2),
    separator("color1"),
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
    round_powerline("color2", "color3"),
    text_icon(fg="color4", bg="color2", text=""),
    separator("color2", padding=7),
    widget.GenPollText(**base(bg="color2", font="Dyuthi Regular"), fontsize=15,
                       func=get_dollar, update_interval=(60*60*12)),
    separator("color2", padding=7000),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
