#!/bin/bash

volumeicon &
nm-applet &
redshift-gtk -l 0:0 -t 4700:4700 &
picom -i .88 -o .92 &
nitrogen --restore
