import tkinter as tk
import subprocess
import executer
from time import sleep


program_to_terminate = "notepad.exe"

class ControlPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Script Control Panel")
        self.geometry("400x300")
        self.configure(bg="#222222")  # Set background color

        # Define your .bat scripts and corresponding commands
        self.scripts = {
            "Enter Blackscreen": "presentation.exe",
            "Start/Restart Killer (may not function properly)": "runner.py"
            # Add more scripts as needed
        }

        self.create_buttons()
        self.create_additional_content()
        self.bind("<Escape>", lambda event: self.destroy())

    def create_buttons(self):
        # Configure button style
        button_style = {
            "font": ("Arial", 12),
            "bg": "#555555",
            "fg": "#FFFFFF",
            "activebackground": "#444444",
            "activeforeground": "#DDDDDD",
            "borderwidth": 0
        }

        for script_name, command in self.scripts.items():
            button = tk.Button(self, text=script_name, command=lambda cmd=command: (executer.run_wo_interrupt(cmd), exit(), sleep(1)), **button_style)
            button.pack(pady=(10, 0), padx=10, fill=tk.X)

        terminate_button = tk.Button(self, text="Manual Blackscreen Termination", command= executer.destroy_smth(program_to_terminate), **button_style)
        terminate_button.pack(pady=(10, 0), padx=10, fill=tk.X)  # Add more padding above the button

    def create_additional_content(self):
        # Add a label below the buttons
        label = tk.Label(self,
                         text="Press the escape key to exit control Panel. \n Drücke die Escape Taste um Control Panel zu beenden.",
                         bg="#222222", fg="white", font=("Arial", 10))
        label.pack(pady=10)

    def run_script(self, command):
        try:
            subprocess.Popen(command, shell=True)
        except Exception as e:
            print(f"Error running script: {e}")


if __name__ == "__main__":
    app = ControlPanel()
    app.mainloop()
