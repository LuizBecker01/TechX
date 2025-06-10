import tkinter as tk

# Cores
FUNDO_VERDE_ESCURO = "#145A32"
TEXTO_BRANCO = "#FFFFFF"
FONTE = ("Arial", 14, "bold")

def cadastrar():
    print("Cadastrar clicado")

def login():
    print("Login clicado")

def sair():
    root.destroy()

root = tk.Tk()
root.title("Tela Principal")
root.configure(bg=FUNDO_VERDE_ESCURO)
root.geometry("400x300")

# Botão Cadastrar
btn_cadastrar = tk.Button(
    root, text="Cadastrar", command=cadastrar,
    bg=FUNDO_VERDE_ESCURO, fg=TEXTO_BRANCO, font=FONTE, width=15
)
btn_cadastrar.pack(pady=20)

# Botão Login
btn_login = tk.Button(
    root, text="Login", command=login,
    bg=FUNDO_VERDE_ESCURO, fg=TEXTO_BRANCO, font=FONTE, width=15
)
btn_login.pack(pady=10)

# Botão Sair
btn_sair = tk.Button(
    root, text="Sair", command=sair,
    bg=FUNDO_VERDE_ESCURO, fg=TEXTO_BRANCO, font=FONTE, width=15
)
btn_sair.pack(pady=10)

root.mainloop()