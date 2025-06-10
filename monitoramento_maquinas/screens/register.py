import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import bcrypt

# Configuração do banco de dados
engine = create_engine('sqlite:///usuarios.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de usuário
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

Base.metadata.create_all(engine)

def hash_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def salvar_usuario(nome, email, senha):
    if session.query(Usuario).filter_by(email=email).first():
        return False, "Email já cadastrado!"
    senha_hash = hash_senha(senha)
    usuario = Usuario(nome=nome, email=email, senha=senha_hash)
    session.add(usuario)
    session.commit()
    return True, "Usuário cadastrado com sucesso!"

def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    if not nome or not email or not senha:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return
    sucesso, msg = salvar_usuario(nome, email, senha)
    if sucesso:
        messagebox.showinfo("Sucesso", msg)
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_senha.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", msg)

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Usuário")
root.geometry("300x300")

tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Senha:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_senha = tk.Entry(root, show="*")
entry_senha.grid(row=2, column=1, padx=10, pady=5)

btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_usuario)
btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()