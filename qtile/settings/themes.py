from os import path
import json
from settings.path import qtile_path

def load_theme(theme="default"):
    theme_file = path.join(qtile_path, "themes", f"{theme}.json")
    if not path.isfile(theme_file):
        print(f"{theme_file} not found")
        return load_theme()

    with open(theme_file, mode="r", encoding="utf-8") as f:
        return json.load(f)

def _create_default_config(config_file_path):
    with open(config_file_path, mode="w", encoding="utf-8") as f:
        json.dump({"theme": "default"}, f)


config_file_path = path.join(qtile_path, "settings.json")
if not path.isfile(config_file_path):
    _create_default_config(config_file_path)
with open(config_file_path, mode="r", encoding="utf-8") as f:
    theme = json.load(f)['theme']
    colors = load_theme(theme)

