#!/bin/bash

volumeicon &
nm-applet &
cbatticon -i symbolic -u 2 -c "systemctl hibernate" -l 15 -r 10 &
picom -i .88 -o .92 &
nitrogen --restore
