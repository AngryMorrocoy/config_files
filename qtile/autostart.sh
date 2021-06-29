#!/bin/bash

udiskie -N &
redshift-gtk -l 0:0 -t 4700:4700 &
xfce4-power-manager &
volumeicon &
nm-applet &
picom &
nitrogen --restore &

