#!/bin/bash

cbatticon -l 30 -r 15 -u 2 --hide-notification -i symbolic -c "echo 3_Arepas | sudo -S safe_poweroff" &
volumeicon &
nm-applet &
redshift-gtk -l 0:0 -t 4700:4700 &
picom -i .88 -o .92 &
nitrogen --restore
