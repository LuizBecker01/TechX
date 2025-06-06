# Tela para cadastro de novas máquinas
import tkinter as tk

class TelaRegister(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        tk.Label(self, text="Tela de Cadastro", font=("Arial", 16)).pack(pady=20)

        tk.Label(self, text="Usuário:").pack(pady=5)
        tk.Entry(self).pack(pady=5)

        tk.Label(self, text="Nome:").pack(pady=5)
        tk.Entry(self).pack(pady=5)

        tk.Label(self, text="Email:").pack(pady=5)
        tk.Entry(self).pack(pady=5)

        tk.Label(self, text="Senha:").pack(pady=5)
        tk.Entry(self, show="*").pack(pady=5)

        tk.Button(self, text="Cadastrar", command=lambda: controller.mostrar_tela("TelaLogin")).pack(pady=10)

        tk.Button(self, text="Voltar", command=lambda: controller.mostrar_tela("TelaPrincipal")).pack(pady=10)
