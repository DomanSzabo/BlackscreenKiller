import tkinter as tk
import subprocess


class ControlPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Script Control Panel")
        self.geometry("400x300")
        self.configure(bg="#222222")  # Set background color

        # Define your .bat scripts and corresponding commands
        self.scripts = {
            "Script 1": "script1.bat",
            "Script 2": "script2.bat",
            "Enter Blackscreen": "presentation.exe",
            # Add more scripts as needed
        }

        self.create_buttons()

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
            button = tk.Button(self, text=script_name, command=lambda cmd=command: self.run_script(cmd), **button_style)
            button.pack(pady=5, padx=10, fill=tk.X)

    def run_script(self, command):
        try:
            subprocess.Popen(command, shell=True)
        except Exception as e:
            print(f"Error running script: {e}")


if __name__ == "__main__":
    app = ControlPanel()
    app.mainloop()