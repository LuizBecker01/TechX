import tkinter as tk
from PIL import Image, ImageTk  # Certifique-se de ter o Pillow instalado
import os

def open_registration():
    # Função chamada ao clicar em "Cadastrar"
    import screens.register  # Importa a tela de cadastro
    screens.register.opens_register_window(root)

def open_login():
    # Função chamada ao clicar em "Entrar"
    import screens.login  # Importa a tela de login
    screens.login.open_login_window(root)

def close_app():
    # Função chamada ao clicar em "Sair"
    root.quit()

# Criação da janela principal
root = tk.Tk()
root.title("Tela Inicial")
root.state("zoomed")  # Tela cheia em qualquer SO
root.configure(bg="#005A3C")  # Define a cor de fundo (Verde Lacoste)

# Cabeçalho na parte superior da janela
header = tk.Frame(root, bg="#00472c", height=50)
header.pack(side="top", fill="x")

header_label = tk.Label(
    header,
    text="TechX • Monitoramento de Máquinas Agrícolas",
    font=("Arial", 16, "bold"),
    bg="#00472c",
    fg="#e6e6e6"
)
header_label.pack(pady=10)

# Frame central para agrupar conteúdo
center = tk.Frame(root, bg="#005A3C")
center.place(relx=0.5, rely=0.5, anchor="center")

# Logo - ajuste o nome do arquivo conforme necessário
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Pasta do script atual
    logo_path = os.path.join(script_dir, "../utils/images/Logo-TechX.png")  # Ajuste conforme a localização real da imagem
    logo_img = Image.open(logo_path)
    print(logo_path)
    # logo_img = Image.open("utils/images/Logo-TechX.png")  # Caminho relativo à pasta do script
    logo_img = logo_img.resize((150, 150), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(center, image=logo_photo, bg="#005A3C")  # Fundo igual ao da tela
    logo_label.image = logo_photo  # Mantém referência para não ser coletado pelo garbage collector
    logo_label.pack(pady=(0, 10))
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    raise

# Título de boas-vindas
welcome_label = tk.Label(
    center,
    text="Bem-vindo!",
    font=("Arial", 16, "bold"),
    bg="#005A3C",
    fg="white"
)
welcome_label.pack(pady=(0, 10))

# Mensagem de impacto centralizada
impact_message = tk.Label(
    center,
    text=(
        "Transforme a gestão do seu campo com tecnologia!\n"
        "Monitore e controle suas máquinas agrícolas remotamente,\n"
        "com informações em tempo real e decisões mais eficientes."
    ),
    font=("Arial", 12),
    bg="#005A3C",
    fg="#e6e6e6",
    justify="center"
)
impact_message.pack(pady=(0, 20))

# Benefícios do sistema
benefits = tk.Label(
    center,
    text="✓ Acesso remoto   ✓ Segurança de dados   ✓ Gestão eficiente",
    font=("Arial", 11, "italic"),
    bg="#005A3C",
    fg="#b7f7d8"
)
benefits.pack(pady=(0, 20))

# Estilo dos botões principais
button_style = {
    "bg": "white",                # Cor de fundo do botão
    "fg": "black",                # Cor do texto do botão
    "font": ("Arial", 12),        # Fonte do texto
    "width": 22,                  # Largura do botão
    "height": 2,                  # Altura do botão
    "bd": 0,                      # Sem borda
    "highlightthickness": 0,      # Sem destaque de borda
    "activebackground": "#e6e6e6" # Cor ao pressionar
}

# Botão para cadastro de usuário
btn_register = tk.Button(center, text="Cadastrar", command=open_registration, **button_style)
btn_register.pack(pady=8)

# Botão para login
btn_login = tk.Button(center, text="Login", command=open_login, **button_style)
btn_login.pack(pady=8)

# Botão para sair do sistema
btn_about = tk.Button(center, text="Sair", command=close_app, **button_style)
btn_about.pack(pady=8)

# Rodapé na parte inferior da janela
footer = tk.Frame(root, bg="#00472c", height=40)
footer.pack(side="bottom", fill="x")

footer_label = tk.Label(
    footer,
    text="© 2025 TechX • Monitoramento inteligente de máquinas agrícolas • Versão 1.0 | Suporte: suporte@techx.com",
    font=("Arial", 10),
    bg="#00472c",
    fg="#e6e6e6"
)
footer_label.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()