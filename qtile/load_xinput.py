#!/usr/bin/python3
import json
import sys
import os

def load_props(props_file="xinput_props.json"):
    try:
        data_file = open(props_file, mode="r", encoding="utf-8")
        return json.load(data_file)
    except FileNotFoundError as e:
        raise e

def set_props(props):
    for device in props:
        for prop, value in props[device].items():
            os.system(f"xinput set-prop {device} {prop} {value}")

if __name__ == '__main__':
    if len( sys.argv ) != 2:
        print("I need one argument, the json file where the configs are")
    CONF_FILE = sys.argv[1]
    PROPS = load_props(CONF_FILE)
    set_props(PROPS)

