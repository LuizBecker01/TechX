import tkinter as tk

COR_PRIMARIA = "#2563eb"
COR_FUNDO = "#f1f5f9"
COR_BOTAO = "#38bdf8"
COR_BOTAO_TXT = "#fff"
FONTE_TITULO = ("Segoe UI", 20, "bold")
FONTE_NORMAL = ("Segoe UI", 12)

class TelaPrincipal(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=COR_FUNDO)
        container = tk.Frame(self, bg=COR_FUNDO)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Bem-vindo ao TechX", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_PRIMARIA).pack(pady=(0, 30))

        estilo_botao = {"font": FONTE_NORMAL, "bg": COR_BOTAO, "fg": COR_BOTAO_TXT, "activebackground": COR_PRIMARIA, "activeforeground": "#fff", "bd": 0, "relief": "flat", "width": 20, "height": 2, "cursor": "hand2"}

        tk.Button(container, text="Entrar", command=lambda: controller.mostrar_tela("TelaLogin"), **estilo_botao).pack(pady=10)
        tk.Button(container, text="Cadastrar", command=lambda: controller.mostrar_tela("TelaRegister"), **estilo_botao).pack(pady=10)
        tk.Button(container, text="Sair", command=controller.destroy, **estilo_botao).pack(pady=10)