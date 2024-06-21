import os
import subprocess as sp

paths = {
    'notepad': "C:\\WINDOWS\\system32\\notepad.exe",
    'browser': "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    "after effects": "C:\\Program Files\\Adobe\\Adobe After Effects 2020\\Support Files\\AfterFX.exe"
}

def open_notepad():
    os.startfile(paths['notepad'])


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_browser():
    os.startfile(paths['browser'])

def After():
    os.startfile(paths['after effects'])