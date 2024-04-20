import psutil
import subprocess


program_path = "math/presentation.exe"
program_name = "notepad.exe"
def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False


while True:
    if is_process_running(program_name):
        subprocess.run(['taskkill', '/F', '/IM', program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run([program_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
