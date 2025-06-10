import tkinter as tk

def open_registration():
    import register  # Import the registration screen

# Criação da janela principal
root = tk.Tk()
root.title("Tela Inicial")
root.geometry("300x200")

welcome_label = tk.Label(root, text="Bem-vindo ao Monitoramento de Máquinas!", font=("Arial", 14))
welcome_label.pack(pady=20)


btn_register = tk.Button(root, text="Cadastrar Usuário", command=open_registration)
btn_register.pack(pady=10)

btn_exit = tk.Button(root, text="Sair", command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()