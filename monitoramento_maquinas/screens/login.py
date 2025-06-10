# Tela de login
import tkinter as tk

COR_PRIMARIA = "#2563eb"
COR_FUNDO = "#f1f5f9"
COR_BOTAO = "#38bdf8"
COR_BOTAO_TXT = "#fff"
FONTE_TITULO = ("Segoe UI", 20, "bold")
FONTE_NORMAL = ("Segoe UI", 12)

class TelaLogin(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=COR_FUNDO)
        container = tk.Frame(self, bg=COR_FUNDO)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Entrar no Sistema", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_PRIMARIA).pack(pady=(0, 20))

        tk.Label(container, text="Email:", font=FONTE_NORMAL, bg=COR_FUNDO).pack(anchor="w")
        self.entry_email = tk.Entry(container, font=FONTE_NORMAL, width=30, relief="flat", highlightbackground=COR_PRIMARIA, highlightcolor=COR_PRIMARIA, highlightthickness=1)
        self.entry_email.pack(pady=(0, 10))

        tk.Label(container, text="Senha:", font=FONTE_NORMAL, bg=COR_FUNDO).pack(anchor="w")
        self.entry_senha = tk.Entry(container, show="*", font=FONTE_NORMAL, width=30, relief="flat", highlightbackground=COR_PRIMARIA, highlightcolor=COR_PRIMARIA, highlightthickness=1)
        self.entry_senha.pack(pady=(0, 20))

        estilo_botao = {"font": FONTE_NORMAL, "bg": COR_BOTAO, "fg": COR_BOTAO_TXT, "activebackground": COR_PRIMARIA, "activeforeground": "#fff", "bd": 0, "relief": "flat", "width": 20, "height": 2, "cursor": "hand2"}

        tk.Button(container, text="Entrar", command=lambda: controller.mostrar_tela("TelaDashboard"), **estilo_botao).pack(pady=5)
        tk.Button(container, text="Voltar", command=lambda: controller.mostrar_tela("TelaPrincipal"), **estilo_botao).pack(pady=5)
