#!/bin/bash

cbatticon -l 30 -r 15 -u 2 -i symbolic &
volumeicon &
nm-applet &
udiskie -N &
redshift-gtk -l 0:0 -t 4700:4700 &
picom -i .88 -o .92 &
nitrogen --restore
