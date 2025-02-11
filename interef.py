import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Interface com Combobox de Estados")
root.geometry("400x350")


tk.Label(root, text="Nome:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_nome = tk.Entry(root, width=30)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada_endereco = tk.Entry(root, width=30)
entrada_endereco.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Bairro:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada_bairro = tk.Entry(root, width=30)
entrada_bairro.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Estado:", font=("Arial", 12)).grid(row=2, column=2, padx=10, pady=5, sticky="e")
opcoes_estados = ["RS", "RJ", "SC"]
combobox_estados = ttk.Combobox(root, values=opcoes_estados)
combobox_estados.grid(row=2, column=3, padx=10, pady=5)
combobox_estados.current(0)  

tk.Label(root, text="Cep:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entrada_cep = tk.Entry(root, width=30)
entrada_cep.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Cidade:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
entrada_cidade = tk.Entry(root, width=30)
entrada_cidade.grid(row=4, column=1, padx=10, pady=5)

label_resultado = tk.Label(root, text="Resultado:", font=("Arial", 12), fg="blue")
label_resultado.grid(row=7, column=0, columnspan=2, pady=10)


def exibir_dados():
    nome = entrada_nome.get()
    endereco = entrada_endereco.get()
    bairro = entrada_bairro.get()
    estado = combobox_estados.get()  
    cep = entrada_cep.get()
    cidade = entrada_cidade.get()

    label_resultado.config(text=f"Nome: {nome}, Endereço: {endereco}, Bairro: {bairro}, Estado: {estado}, Cep: {cep}, Cidade: {cidade}")


botao_exibir = tk.Button(root, text="Exibir", command=exibir_dados)
botao_exibir.grid(row=8, column=1, padx=10, pady=10)

root.mainloop()
