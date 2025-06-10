# Tela para cadastro
import tkinter as tk
from db_config import Session
from models.Usuario import Usuario, add_usuario


class TelaRegister(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.session = Session


    def registrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        usuario = Usuario(nome=nome, email=email, senha=senha)
        add_usuario(usuario, self.session)
        print("Usuário registrado!")
        self.controller.mostrar_tela("TelaLogin")
