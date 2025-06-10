# Tela de login
import tkinter as tk
import bcrypt

def login_usuario(email, senha):
    usuario = session.query(Usuario).filter_by(email=email).first()
    if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario.senha.encode('utf-8')):
        return True, "Login bem-sucedido!"
    return False, "Email ou senha incorretos!"

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

root.mainloop()