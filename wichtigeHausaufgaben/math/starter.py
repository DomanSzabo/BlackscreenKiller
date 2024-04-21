import subprocess


def runSmth(name):
    if ".py" in name:
        print("got here")
        subprocess.run(["python", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.run([name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def run_wo_interrupt(name):
    if ".py" in name:
        print("got here")
        subprocess.Popen(["python", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen([name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == "__main__":
    run_wo_interrupt("runner.py")