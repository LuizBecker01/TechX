# Tela principal com listagem e status das máquinas
import tkinter as tk

COR_PRIMARIA = "#2563eb"
COR_SECUNDARIA = "#1e293b"
COR_FUNDO = "#f1f5f9"
COR_BOTAO = "#38bdf8"
COR_BOTAO_TXT = "#fff"
FONTE_TITULO = ("Segoe UI", 18, "bold")
FONTE_NORMAL = ("Segoe UI", 12)

class TelaDashboard(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=COR_FUNDO)

        # Menu lateral
        menu = tk.Frame(self, width=200, bg=COR_SECUNDARIA)
        menu.pack(side="left", fill="y")

        estilo_menu = {"font": FONTE_NORMAL, "bg": COR_SECUNDARIA, "fg": "#fff", "activebackground": COR_PRIMARIA, "activeforeground": "#fff", "bd": 0, "relief": "flat", "width": 20, "height": 2, "cursor": "hand2"}

        tk.Label(menu, text="Menu", font=FONTE_TITULO, bg=COR_SECUNDARIA, fg=COR_BOTAO).pack(pady=(30, 20))
        tk.Button(menu, text="Histórico", **estilo_menu).pack(pady=5)
        tk.Button(menu, text="Info em tempo real", **estilo_menu).pack(pady=5)
        tk.Button(menu, text="Dados do usuário", **estilo_menu).pack(pady=5)
        tk.Button(menu, text="Info do veículo", **estilo_menu).pack(pady=5)
        tk.Button(menu, text="Sair", command=lambda: controller.mostrar_tela("TelaPrincipal"), **estilo_menu).pack(pady=(40, 5))

        # Área de conteúdo
        self.content = tk.Frame(self, bg=COR_FUNDO)
        self.content.pack(side="left", fill="both", expand=True)
        tk.Label(self.content, text="Informações do Veículo", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_PRIMARIA).pack(pady=30)
        # Adicione aqui widgets para mostrar os dados do veículo
