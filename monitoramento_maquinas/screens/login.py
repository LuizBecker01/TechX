# Tela de login
import tkinter as tk
import bcrypt

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
    tk.messagebox.showinfo("Resultado", mensagem)

root = tk.Tk()
root.title("Login de Usuário")
root.geometry("300x300")

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Senha:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_senha = tk.Entry(root, show="*")
entry_senha.grid(row=2, column=1, padx=10, pady=5)

btn_login = tk.Button(root, text="Entrar", command=login_usuario)
btn_login.grid(row=3, column=0, columnspan=2, pady=10)

btn_sair = tk.Button(root, text="Sair", command=root.quit)
btn_sair.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()