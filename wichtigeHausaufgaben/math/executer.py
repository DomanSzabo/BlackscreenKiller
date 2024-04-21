import subprocess


def runSmth(name):
    if ".py" in name:
        subprocess.run(["python", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.run([name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def run_wo_interrupt(name):
    if ".py" in name:
        subprocess.Popen(["python", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        subprocess.Popen([name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def destroy_smth(name):
    subprocess.run(['taskkill', '/F', '/IM', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
