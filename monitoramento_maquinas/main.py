import tkinter as tk
from screens.principal import TelaPrincipal
from screens.login import TelaLogin
from screens.register import TelaRegister
from screens.dashboard import TelaDashboard
from screens.historics import TelaHistorics

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TechX Monitoramento")
        self.geometry("300x700")
        self.config(bg="lightblue")
        self.frames = {}

        # Cria e guarda as telas no dicionário
        for Tela in (TelaPrincipal, TelaLogin, TelaRegister, TelaDashboard, TelaHistorics):
            frame = Tela(self, self)
            self.frames[Tela.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostra a primeira tela
        self.mostrar_tela("TelaPrincipal")

    def mostrar_tela(self, nome_tela):
        frame = self.frames[nome_tela]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
