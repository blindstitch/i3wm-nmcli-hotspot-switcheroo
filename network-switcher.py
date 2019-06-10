#!/usr/bin/env python3
# Toggle between personal hotspot and available stored networks, with a priority option

from i3 import *
import subprocess

app_name = 'Network switcher'

networks = {
    'hotspot': 'my_hotspot',
    'priority': 'my_home_network'
}

nm_cmds = {
    'current' : ['nmcli', '-t', '-f', 'NAME', 'connection', 'show', '--active'],
    'stored' : ['nmcli', '-t', '-f', 'NAME', 'connection', 'show'],
    'avail' : ['nmcli', '-t', '-f', 'SSID', 'device', 'wifi', 'list'],
    'rescan' : ['nmcli', 'device', 'wifi', 'rescan'],
    'connect' : ['nmcli', 'con', 'up', 'id'],
}

subprocess.call(nm_cmds['rescan'])

def wlan_connect(network):
    subprocess.call(nm_cmds['connect'] + [network])

nm_out = {}
for command_name in ['current','stored','avail']:
    command = subprocess.Popen(nm_cmds[command_name],stdout=PIPE)
    stdout = command.communicate()[0].decode('utf-8')
    stdout = stdout.split('\n')[:-1]
    if command_name == 'current':
        stdout = stdout[0]
    nm_out[command_name] = stdout

storedavailablenets = [a for a in nm_out['avail'] if a in nm_out['stored'] and a != networks['hotspot']]

if nm_out['current'] == networks['hotspot']:
    if len(storedavailablenets) == 0:
        notify(app_name,'Connected to hotspot, but there are no other available networks.')
    else:
        if networks['priority'] in storedavailablenets:
            notify_text = 'Disconnecting from hotspot.\nAttempting to connect to priority network "' + networks['priority'] + '"'
            notify(app_name,notify_text)
            wlan_connect(networks['priority'])
        else:
            notify_text = 'Disconnecting from hotspot.\nAttempting to connect to non-priority network "' + storedavailablenets[0] + '"'
            notify(app_name,notify_text)
            wlan_connect(storedavailablenets[0])
else:
    if networks['hotspot'] in nm_out['avail']:
        notify_text = 'Attempting to connect to the hotspot "' + networks['hotspot'] + '"'
        notify(app_name,notify_text)
        wlan_connect(networks['hotspot'])
    else:
        notify(app_name,'The hotspot "'+networks['hotspot']+'" is not available')
