import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import bcrypt
import os

# --- Cores e fontes do sistema ---
COR_PRIMARIA = "#005A3C"
COR_HEADER = "#00472c"
COR_TEXTO = "white"
COR_LABEL = "#e6e6e6"
COR_BOTAO = "white"
COR_BOTAO_TXT = "black"
COR_BOTAO_ATIVO = "#e6e6e6"
FONTE_TITULO = ("Arial", 18, "bold")
FONTE_LABEL = ("Arial", 12)
FONTE_BOTAO = ("Arial", 12)

# --- Banco de dados ---
engine = create_engine('sqlite:///usuarios.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

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

# --- Janela principal ---
root = tk.Tk()
root.title("Cadastro de Usuário")
root.geometry("600x500")
root.configure(bg=COR_PRIMARIA)

# Cabeçalho
header = tk.Frame(root, bg=COR_HEADER, height=50)
header.pack(side="top", fill="x")
header_label = tk.Label(
    header,
    text="TechX • Cadastro de Usuário",
    font=FONTE_TITULO,
    bg=COR_HEADER,
    fg=COR_LABEL
)
header_label.pack(pady=10)

# Frame central para centralizar o formulário
center = tk.Frame(root, bg=COR_PRIMARIA)
center.place(relx=0.5, rely=0.5, anchor="center")

# Título do formulário
form_title = tk.Label(center, text="Crie sua conta", font=FONTE_TITULO, bg=COR_PRIMARIA, fg=COR_LABEL)
form_title.pack(pady=(0, 20))

# Campos do formulário
label_nome = tk.Label(center, text="Nome:", font=FONTE_LABEL, bg=COR_PRIMARIA, fg=COR_LABEL)
label_nome.pack(anchor="w")
entry_nome = tk.Entry(center, font=FONTE_LABEL, width=30, relief="flat", highlightbackground=COR_HEADER, highlightcolor=COR_HEADER, highlightthickness=1)
entry_nome.pack(pady=(0, 10))

label_email = tk.Label(center, text="Email:", font=FONTE_LABEL, bg=COR_PRIMARIA, fg=COR_LABEL)
label_email.pack(anchor="w")
entry_email = tk.Entry(center, font=FONTE_LABEL, width=30, relief="flat", highlightbackground=COR_HEADER, highlightcolor=COR_HEADER, highlightthickness=1)
entry_email.pack(pady=(0, 10))

label_senha = tk.Label(center, text="Senha:", font=FONTE_LABEL, bg=COR_PRIMARIA, fg=COR_LABEL)
label_senha.pack(anchor="w")
entry_senha = tk.Entry(center, show="*", font=FONTE_LABEL, width=30, relief="flat", highlightbackground=COR_HEADER, highlightcolor=COR_HEADER, highlightthickness=1)
entry_senha.pack(pady=(0, 20))

# Botão cadastrar
btn_cadastrar = tk.Button(
    center,
    text="Cadastrar",
    command=cadastrar_usuario,
    bg=COR_BOTAO,
    fg=COR_BOTAO_TXT,
    font=FONTE_BOTAO,
    width=22,
    height=2,
    bd=0,
    highlightthickness=0,
    activebackground=COR_BOTAO_ATIVO
)
btn_cadastrar.pack(pady=10)

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