# Tela de login
import tkinter as tk

class TelaLogin(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        tk.Label(self, text="Tela de Login", font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Voltar", command=lambda: controller.mostrar_tela("TelaPrincipal")).pack(pady=10)
