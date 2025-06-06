import tkinter as tk

class TelaPrincipal(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        # Configurar o layout do frame principal (self) usando grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Criar um frame interno centralizado
        container = tk.Frame(self)
        container.grid(row=1, column=0)

        # Conteúdo centralizado dentro do container
        rotulo_titulo = tk.Label(container, text="TechX", font=("Arial", 18, "bold"))
        rotulo_titulo.pack(pady=10)

        rotulo_texto = tk.Label(
            container,
            text="Bem-vindo ao Monitoramento de Máquinas da TechX,\npor favor efetue o login para continuar",
            font=("Arial", 12),
            wraplength=400,
            justify="center"
        )
        rotulo_texto.pack(pady=15)

        botao_cadastrar = tk.Button(
            container,
            text="Cadastrar",
            font=("Arial", 12),
            command=lambda: controller.mostrar_tela("TelaRegister")
        )
        botao_cadastrar.pack(pady=5)

        botao_login = tk.Button(
            container,
            text="Login",
            font=("Arial", 12),
            command=lambda: controller.mostrar_tela("TelaLogin")
        )
        botao_login.pack(pady=5)
