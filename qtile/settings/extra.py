import subprocess
import requests
import re
from bs4 import BeautifulSoup


def window_to_next_group(qtile):
    """Swithcs the actual window to the next group"""
    group_names = [x.name for x in qtile.groups]
    current_group = qtile.current_group.name
    next_group = qtile.groups[(group_names.index(current_group) + 1) % len(group_names)]
    qtile.current_window.cmd_togroup(next_group.name)

    qtile.current_screen.toggle_group(next_group)


def window_to_prev_group(qtile):
    """Swithcs the actual window to the previous group"""
    group_names = [x.name for x in qtile.groups]
    current_group = qtile.current_group.name
    next_group = qtile.groups[(group_names.index(current_group) - 1) % len(group_names)]
    qtile.current_window.cmd_togroup(next_group.name)

    qtile.current_screen.toggle_group(next_group)


def move_floating(qtile, dx, dy):
    """Function for moving floating windows, only if they're floating"""
    curr_window_info = qtile.current_window.info()
    if curr_window_info["floating"]:
        qtile.current_window.cmd_move_floating(dx, dy)


def resize_floating(qtile, dw, dh):
    """Function for resizing floating windows, only if they're floating"""
    curr_window_info = qtile.current_window.info()
    if curr_window_info["floating"]:
        qtile.current_window.cmd_resize_floating(dw, dh)


def get_dollar():
    '''This functions just do web scrapping to get the actual price of the dollar in BsF'''
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
    '''This functions returns an unicode formated battery status'''
    ICONS = {
        "C": [x+" " for x in ""],
        "D": [x+"  " for x in ""],
        "U": [x+"  " for x in ""],
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

