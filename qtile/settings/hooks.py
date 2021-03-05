from libqtile import hook
from .path import path
from os import path
import subprocess

@hook.subscribe.startup_once
def load_external_conf():
    # Called once per start, extra configuration
    script_file = path.join(qtile_path, "load_xinput.py")
    config_file = path.join(qtile_path, "xinput_props.json")

    subprocess.call([script_file, config_file])
    subprocess.call(path.join(qtile_path, "autostart.sh"))

@hook.subscribe.startup_complete
def on_startup():
    subprocess.call(["xsetroot", "-cursor_name", "left_ptr"])

@hook.subscribe.client_focus
def on_focus_change(window):
    """Brings to front a floating windows when focused"""
    if window.info()["floating"]:
        window.cmd_bring_to_front()

