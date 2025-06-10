import tkinter as tk

def open_registration():
    import register  # Import the registration screen

def open_login():
    import login  # Import the login screen

def close_app():
    root.quit()

# Criação da janela principal
root = tk.Tk()
root.title("Tela Inicial")
root.geometry("350x300")
root.configure(bg="#005A3C")  # Verde Lacoste

welcome_label = tk.Label(
    root,
    text="Bem-vindo ao Monitoramento de Máquinas!",
    font=("Arial", 14),
    bg="#005A3C",
    fg="white"
)
welcome_label.pack(pady=30)

button_style = {
    "bg": "white",
    "fg": "black",
    "font": ("Arial", 12),
    "width": 22,
    "height": 2,
    "bd": 0,
    "highlightthickness": 0,
    "activebackground": "#e6e6e6"
}

btn_register = tk.Button(root, text="Cadastrar", command=open_registration, **button_style)
btn_register.pack(pady=8)

btn_login = tk.Button(root, text="Entrar", command=open_login, **button_style)
btn_login.pack(pady=8)

btn_about = tk.Button(root, text="Sair", command=close_app, **button_style)
btn_about.pack(pady=8)

root.mainloop()