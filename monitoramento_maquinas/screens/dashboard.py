 # Tela principal com listagem e status das máquinas
import tkinter as tk

class TelaDashboard(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        tk.Label(self, text="Dashboard", font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Históricos", command=lambda: controller.mostrar_tela("TelaHistoricos")).pack(pady=10)
        tk.Button(self, text="Logout", command=lambda: controller.mostrar_tela("TelaPrincipal")).pack(pady=10)
