# Tela para cadastro de novas máquinas
import tkinter as tk

class TelaRegister(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        tk.Label(self, text="Tela de Cadastro", font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Voltar", command=lambda: controller.mostrar_tela("TelaPrincipal")).pack(pady=10)
