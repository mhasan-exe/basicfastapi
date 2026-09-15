import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")

def button_callback():
    print("button cicked!")
    pass
button = ctk.CTkButton(
    master=app,
    command= button_callback
)

button.pack(padx=20, pady=20)
app.mainloop()