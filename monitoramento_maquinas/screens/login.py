# Tela de login
import tkinter as tk

class TelaLogin(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        tk.Label(self, text="Login", font=("Arial", 16)).pack(pady=20)

        tk.Label(self, text="Usuário:").pack(pady=5)
        tk.Entry(self).pack(pady=5)

        tk.Label(self, text="Senha:").pack(pady=5)
        tk.Entry(self, show="*").pack(pady=5)

        tk.Button(self, text="Entrar", command=lambda: controller.mostrar_tela("TelaDashboard")).pack(pady=10)

        tk.Button(self, text="Voltar", command=lambda: controller.mostrar_tela("TelaPrincipal")).pack(pady=10)
