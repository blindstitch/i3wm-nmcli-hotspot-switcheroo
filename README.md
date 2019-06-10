# Network hotspot switcher for `nmcli`

My internet at home is unreliable; I switch between my hotspot and my home network constantly.
This script detects which network is connected and issues the appropriate commands to `nmcli` to switch between them.
A notification is posted via `notify-send` of network status.

## requires

 - `nmcli`
 - `notify-send` (tested on Ubuntu-Gnome)

## usage

`python3 ./wifi-switcher.py`

## TODO

 - `argparse` to specify preferred and hotspot for configuration within i3 config file
 - A time delay is needed after the `avail` command is issued, so that the list is known when the script runs. You may need to occasionally run the script twice.
 - Add `print` commands to accompany notifications
