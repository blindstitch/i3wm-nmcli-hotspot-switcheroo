# i3 wrapper

from subprocess import Popen, PIPE, run, call
from json import loads
from sys import argv

def get_tree():
    command = ['i3-msg','-t','get_tree']
    process = Popen(command,stdout=PIPE)
    string = process.communicate()[0].decode('utf-8')
    return loads(string)

def get_spaces():
    command = ['i3-msg','-t','get_workspaces']
    process = Popen(command,stdout=PIPE)
    string = process.communicate()[0].decode('utf-8')
    return loads(string)

def get_active_space():
    spaces = get_spaces()
    return spaces.index(list(filter(lambda x: x['focused'] == True,spaces))[0])

def notify(title,text):
    command = ['notify-send', '--icon=gtk-info', title, text]
    call(command)
