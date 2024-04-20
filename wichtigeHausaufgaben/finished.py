import psutil
import subprocess
import keyboard


fake_blackscreen_path = "math/presentation.exe"
control_panel_path = "math/controlPanel.py"
program_name = "notepad.exe"
control_panel_shortcut = "ctrl + shift + w"
def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False


while True:
    if is_process_running(program_name):
        subprocess.run(['taskkill', '/F', '/IM', program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run([fake_blackscreen_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if keyboard.is_pressed(control_panel_shortcut):
        subprocess.run(["python", control_panel_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)
