import tkinter as tk

class TelaHistorics(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        label = tk.Label(self, text="Tela de Históricos", font=("Arial", 16))
        label.pack(pady=20)

        botao_voltar = tk.Button(
            self,
            text="Voltar",
            command=lambda: controller.mostrar_tela("TelaPrincipal")
        )
        botao_voltar.pack(pady=10)
