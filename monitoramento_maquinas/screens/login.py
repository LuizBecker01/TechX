# Tela de login estilizada
import tkinter as tk
from tkinter import messagebox
import bcrypt

# Cores e fontes do sistema
COR_PRIMARIA = "#005A3C"
COR_HEADER = "#00472c"
COR_LABEL = "#e6e6e6"
COR_BOTAO = "white"
COR_BOTAO_TXT = "black"
COR_BOTAO_ATIVO = "#e6e6e6"
FONTE_TITULO = ("Arial", 18, "bold")
FONTE_LABEL = ("Arial", 12)
FONTE_BOTAO = ("Arial", 12)

def verificar_login(email, senha):
    # Aqui você faz a verificação do usuário e senha
    if email == "admin" and senha == "123":
        return True, "Login realizado com sucesso!"
    else:
        return False, "Email ou senha incorretos."

def login_usuario():
    email = entry_email.get()
    senha = entry_senha.get()
    sucesso, mensagem = verificar_login(email, senha)
    messagebox.showinfo("Resultado", mensagem)

# Janela principal
root = tk.Tk()
root.title("Login de Usuário")
root.geometry("400x350")
root.configure(bg=COR_PRIMARIA)

# Cabeçalho
header = tk.Frame(root, bg=COR_HEADER, height=50)
header.pack(side="top", fill="x")
header_label = tk.Label(
    header,
    text="TechX • Login",
    font=FONTE_TITULO,
    bg=COR_HEADER,
    fg=COR_LABEL
)
header_label.pack(pady=10)

# Frame central para centralizar o formulário
center = tk.Frame(root, bg=COR_PRIMARIA)
center.place(relx=0.5, rely=0.5, anchor="center")

# Campos do formulário
label_email = tk.Label(center, text="Email:", font=FONTE_LABEL, bg=COR_PRIMARIA, fg=COR_LABEL)
label_email.pack(anchor="w")
entry_email = tk.Entry(center, font=FONTE_LABEL, width=30, relief="flat", highlightbackground=COR_HEADER, highlightcolor=COR_HEADER, highlightthickness=1)
entry_email.pack(pady=(0, 10))

label_senha = tk.Label(center, text="Senha:", font=FONTE_LABEL, bg=COR_PRIMARIA, fg=COR_LABEL)
label_senha.pack(anchor="w")
entry_senha = tk.Entry(center, show="*", font=FONTE_LABEL, width=30, relief="flat", highlightbackground=COR_HEADER, highlightcolor=COR_HEADER, highlightthickness=1)
entry_senha.pack(pady=(0, 20))

# Botão entrar
btn_login = tk.Button(
    center,
    text="Entrar",
    command=login_usuario,
    bg=COR_BOTAO,
    fg=COR_BOTAO_TXT,
    font=FONTE_BOTAO,
    width=22,
    height=2,
    bd=0,
    highlightthickness=0,
    activebackground=COR_BOTAO_ATIVO
)
btn_login.pack(pady=8)

# Botão sair
btn_sair = tk.Button(
    center,
    text="Sair",
    command=root.quit,
    bg=COR_BOTAO,
    fg=COR_BOTAO_TXT,
    font=FONTE_BOTAO,
    width=22,
    height=2,
    bd=0,
    highlightthickness=0,
    activebackground=COR_BOTAO_ATIVO
)
btn_sair.pack(pady=8)

# Rodapé
footer = tk.Frame(root, bg=COR_HEADER, height=40)
footer.pack(side="bottom", fill="x")
footer_label = tk.Label(
    footer,
    text="© 2025 TechX • Monitoramento inteligente de máquinas agrícolas • Versão 1.0",
    font=("Arial", 10),
    bg=COR_HEADER,
    fg=COR_LABEL
)
footer_label.pack(pady=10)

root.mainloop()