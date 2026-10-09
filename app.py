import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x300")

def button_callback():
    print("button cicked!")
    pass
def buttonpress2():
    print("2")

button = ctk.CTkButton(
    master=app,
    command= button_callback
)
button2 = ctk.CTkButton(
    master=app,
    command=buttonpress2,
    text=2
)
button.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)
app.mainloop()