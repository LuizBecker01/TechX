import tkinter as tk
from screens.principal import TelaPrincipal
from screens.login import TelaLogin
from screens.register import TelaRegister
from screens.dashboard import TelaDashboard
from screens.historics import TelaHistorics

COR_PRIMARIA = "#2563eb"      # Azul principal
COR_SECUNDARIA = "#1e293b"    # Cinza escuro
COR_FUNDO = "#f1f5f9"         # Cinza claro
COR_BOTAO = "#38bdf8"         # Azul claro
COR_BOTAO_TXT = "#fff"
FONTE_TITULO = ("Segoe UI", 20, "bold")
FONTE_NORMAL = ("Segoe UI", 12)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TechX Monitoramento")
        self.geometry("900x550")
        self.config(bg=COR_FUNDO)
        self.frames = {}

        # Frame principal de conteúdo
        self.content_frame = tk.Frame(self, bg=COR_FUNDO)
        self.content_frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Cria e guarda as telas no dicionário
        for Tela in (TelaPrincipal, TelaLogin, TelaRegister, TelaDashboard, TelaHistorics):
            frame = Tela(self.content_frame, self)
            self.frames[Tela.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("TelaPrincipal")  # Tela inicial com opções

    def mostrar_tela(self, nome_tela):
        frame = self.frames[nome_tela]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
