#!/usr/bin/env bash

xrandr --output eDP-1 --mode "1920x1080" --rate "60.01"
xrandr --output eDP-2 --mode "1920x1080" --rate "60.01"
xrandr --output eDP-3 --mode "1920x1080" --rate "60.01"
xrandr --output Virtual-1 --mode "1920x1080" --rate "60.01"
xrandr --output Virtual-2 --mode "1920x1080" --rate "60.01"
xrandr --output Virtual-3 --mode "1920x1080" --rate "60.01"
picom &
wal -R 
copyq &
xset s off
xset s noblank
xset -dpms
xset +fp /home/ste/.local/share/fonts
xset fp rehash
xset +fp /home/ste/sdots/.local/share/fonts
xset fp rehash
xss-lock -- betterlockscreen -c 000000 &
dunst &
nm-applet &
blueman-applet &
flameshot &
jamesdsp --tray &
libinput-gestures &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xset r rate 220 40
