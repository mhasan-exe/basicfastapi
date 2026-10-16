import customtkinter as ctk
import subprocess

app = ctk.CTk()
app.geometry("500x300")

def button_callback():
    print("button clicked!")
    pass
def buttonpress2():
    app_path = r"C:\Windows\System32\notepad.exe"
    subprocess.Popen([app_path])
def buttonpress3():
    app_path = r"C:\Windows\System32\cmd.exe"
    subprocess.Popen([app_path])

button = ctk.CTkButton(
    master=app,
    command= button_callback
)
button2 = ctk.CTkButton(
    master=app,
    command=buttonpress2,
    text="Notepad"
)
button3 = ctk.CTkButton(
    master=app,
    command=buttonpress3,
    text="cmd"
)
button.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)
button3.pack(padx=20, pady=20)
app.mainloop()