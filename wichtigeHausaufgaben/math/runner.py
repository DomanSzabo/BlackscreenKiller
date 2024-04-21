import psutil
import subprocess
import keyboard
import win32gui
from time import sleep
import starter

fake_blackscreen_path = "presentation.exe"
fake_py_blackscreen_path = "presentation.py"
control_panel_path = "controlPanel.py"
control_panel_exe_path = "controlPanel.exe"
program_name = "notepad.exe"
control_panel_shortcut = "ctrl + shift + w"


hwnd = win32gui.GetForegroundWindow()

# Modify the window's position
#win32gui.MoveWindow(hwnd, 300, 400, 1, 1, True)


def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

while True:
    if is_process_running(program_name):
        subprocess.run(['taskkill', '/F', '/IM', program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        starter.run_wo_interrupt(fake_blackscreen_path)
    if keyboard.is_pressed(control_panel_shortcut):
        starter.run_wo_interrupt(control_panel_path)
    sleep(1)