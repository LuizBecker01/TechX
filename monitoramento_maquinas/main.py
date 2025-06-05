# Arquivo principal para rodar o app
import tkinter as tk

janela = tk.Tk()
janela.geometry("600x400")

rotulo = tk.Label(janela, text="TechX", font=("Arial", 18, "bold"))
rotulo.pack(pady=10)

rotulo = tk.Label(
    janela,
    text="Bem-vindo ao Monitoramento de Máquinas da TechX, por favor efetue o login para continuar",
    font=("Arial", 12),
    wraplength=400  # ← ajusta conforme o tamanho da sua janela
)
rotulo.pack(pady=15, padx=15)


botao_cadastrar = tk.Button(janela, text="Cadasrtrar", font=("Arial", 12))
botao_cadastrar.pack(side=tk.TOP, pady=10)

botao_entrar = tk.Button(janela, text="Entrar", font=("Arial", 12))
botao_entrar.pack(side=tk.TOP, pady=10)


janela.mainloop()