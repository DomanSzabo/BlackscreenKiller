import psutil
import subprocess
import keyboard
import win32gui
from time import sleep
import executer

fake_blackscreen_exe_path = "presentation.exe"
fake_blackscreen_py_path = "presentation.py"
control_panel_py_path = "controlPanel.py"
control_panel_exe_path = "controlPanel.exe"
program_name = "notepad.exe"
control_panel_shortcut = "ctrl + shift + w"
exit_killer_shortcut = "ctrl + shift + q"


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
        executer.destroy_smth(program_name)
        executer.run_wo_interrupt(fake_blackscreen_exe_path)
    if keyboard.is_pressed(control_panel_shortcut):
        executer.run_wo_interrupt(control_panel_py_path)
    elif keyboard.is_pressed(exit_killer_shortcut):
        break
    sleep(1)