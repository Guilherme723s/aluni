import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ClientForm:
    def __init__(self, master):
        self.master = master
        master.title("d0f0c0")

        # Cor de fundo verde clarinho para a janela inteira
        master.configure(bg="#d0f0c0")  # Verde claro para o fundo da janela
        
        # Create a frame for the form fields with no background to keep the window background
        self.form_frame = tk.Frame(master, bg="#d0f0c0")  # Cor do fundo da frame
        self.form_frame.pack(pady=10, padx=20)

        # Primeira Linha: CPF/CNPJ, Nome e Razão Social
        self.cpf_label = tk.Label(self.form_frame, text="CPF/CNPJ:", bg="#d0f0c0")
        self.cpf_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.cpf_entry = tk.Entry(self.form_frame)
        self.cpf_entry.grid(row=0, column=1, padx=5, pady=5)

        self.name_label = tk.Label(self.form_frame, text="Nome:", bg="#d0f0c0")
        self.name_label.grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)

        self.razao_label = tk.Label(self.form_frame, text="Razão Social:", bg="#d0f0c0")
        self.razao_label.grid(row=0, column=4, sticky="e", padx=5, pady=5)
        self.razao_entry = tk.Entry(self.form_frame)
        self.razao_entry.grid(row=0, column=5, padx=5, pady=5)

        # Segunda Linha: Pessoa, Contato, Telefone, Celular, Fax
        self.pessoa_label = tk.Label(self.form_frame, text="Pessoa:", bg="#d0f0c0")
        self.pessoa_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.pessoa_var = tk.StringVar(self.master)
        self.pessoa_var.set("Física")  # Default value
        self.pessoa_menu = tk.OptionMenu(self.form_frame, self.pessoa_var, "Física", "Jurídica")
        self.pessoa_menu.grid(row=1, column=1, padx=5, pady=5)

        self.contato_label = tk.Label(self.form_frame, text="Contato:", bg="#d0f0c0")
        self.contato_label.grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.contato_entry = tk.Entry(self.form_frame)
        self.contato_entry.grid(row=1, column=3, padx=5, pady=5)

        self.telefone_label = tk.Label(self.form_frame, text="Telefone:", bg="#d0f0c0")
        self.telefone_label.grid(row=1, column=4, sticky="e", padx=5, pady=5)
        self.telefone_entry = tk.Entry(self.form_frame)
        self.telefone_entry.grid(row=1, column=5, padx=5, pady=5)

        self.celular_label = tk.Label(self.form_frame, text="Celular:", bg="#d0f0c0")
        self.celular_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.celular_entry = tk.Entry(self.form_frame)
        self.celular_entry.grid(row=2, column=1, padx=5, pady=5)

        self.fax_label = tk.Label(self.form_frame, text="Fax:", bg="#d0f0c0")
        self.fax_label.grid(row=2, column=2, sticky="e", padx=5, pady=5)
        self.fax_entry = tk.Entry(self.form_frame)
        self.fax_entry.grid(row=2, column=3, padx=5, pady=5)

        # Terceira Linha: Data de Nascimento, Sexo, Inscrição Estadual, Documento, Categoria
        self.data_nasc_label = tk.Label(self.form_frame, text="Data Nascimento:", bg="#d0f0c0")
        self.data_nasc_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.data_nasc_entry = tk.Entry(self.form_frame)
        self.data_nasc_entry.grid(row=3, column=1, padx=5, pady=5)

        self.sexo_label = tk.Label(self.form_frame, text="Sexo:", bg="#d0f0c0")
        self.sexo_label.grid(row=3, column=2, sticky="e", padx=5, pady=5)
        self.sexo_var = tk.StringVar(self.master)
        self.sexo_var.set("Masculino")  # Default value
        self.sexo_menu = tk.OptionMenu(self.form_frame, self.sexo_var, "Masculino", "Feminino")
        self.sexo_menu.grid(row=3, column=3, padx=5, pady=5)

        self.inscricao_estadual_label = tk.Label(self.form_frame, text="Inscrição Estadual:", bg="#d0f0c0")
        self.inscricao_estadual_label.grid(row=3, column=4, sticky="e", padx=5, pady=5)
        self.inscricao_estadual_entry = tk.Entry(self.form_frame)
        self.inscricao_estadual_entry.grid(row=3, column=5, padx=5, pady=5)

        self.doc_label = tk.Label(self.form_frame, text="Documento:", bg="#d0f0c0")
        self.doc_label.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.doc_entry = tk.Entry(self.form_frame)
        self.doc_entry.grid(row=4, column=1, padx=5, pady=5)

        self.categoria_label = tk.Label(self.form_frame, text="Categoria:", bg="#d0f0c0")
        self.categoria_label.grid(row=4, column=2, sticky="e", padx=5, pady=5)
        self.categoria_entry = tk.Entry(self.form_frame)
        self.categoria_entry.grid(row=4, column=3, padx=5, pady=5)

        # Caixa de seleção para Optante Simples
        self.optante_var = tk.IntVar()
        self.optante_check = tk.Checkbutton(self.form_frame, text="Optante Simples", variable=self.optante_var, bg="#d0f0c0")
        self.optante_check.grid(row=4, column=4, columnspan=2, sticky="w", padx=5, pady=5)

        # Quarta Linha: Endereço do Cliente
        self.endereco_label = tk.Label(self.form_frame, text="Endereço do Cliente:", bg="#d0f0c0")
        self.endereco_label.grid(row=5, column=0, sticky="e", columnspan=2, padx=5, pady=5)
        
        self.cep_label = tk.Label(self.form_frame, text="CEP:", bg="#d0f0c0")
        self.cep_label.grid(row=6, column=0, sticky="e", padx=5, pady=5)
        self.cep_entry = tk.Entry(self.form_frame)
        self.cep_entry.grid(row=6, column=1, padx=5, pady=5)

        self.endereco_label = tk.Label(self.form_frame, text="Endereço:", bg="#d0f0c0")
        self.endereco_label.grid(row=6, column=2, sticky="e", padx=5, pady=5)
        self.endereco_entry = tk.Entry(self.form_frame)
        self.endereco_entry.grid(row=6, column=3, padx=5, pady=5)

        self.numero_label = tk.Label(self.form_frame, text="Número:", bg="#d0f0c0")
        self.numero_label.grid(row=6, column=4, sticky="e", padx=5, pady=5)
        self.numero_entry = tk.Entry(self.form_frame)
        self.numero_entry.grid(row=6, column=5, padx=5, pady=5)

        self.complemento_label = tk.Label(self.form_frame, text="Complemento:", bg="#d0f0c0")
        self.complemento_label.grid(row=7, column=0, sticky="e", padx=5, pady=5)
        self.complemento_entry = tk.Entry(self.form_frame)
        self.complemento_entry.grid(row=7, column=1, padx=5, pady=5)

        self.bairro_label = tk.Label(self.form_frame, text="Bairro:", bg="#d0f0c0")
        self.bairro_label.grid(row=7, column=2, sticky="e", padx=5, pady=5)
        self.bairro_entry = tk.Entry(self.form_frame)
        self.bairro_entry.grid(row=7, column=3, padx=5, pady=5)

        self.estado_label = tk.Label(self.form_frame, text="Estado:", bg="#d0f0c0")
        self.estado_label.grid(row=7, column=4, sticky="e", padx=5, pady=5)
        self.estado_entry = tk.Entry(self.form_frame)
        self.estado_entry.grid(row=7, column=5, padx=5, pady=5)

        self.cidade_label = tk.Label(self.form_frame, text="Cidade:", bg="#d0f0c0")
        self.cidade_label.grid(row=8, column=0, sticky="e", padx=5, pady=5)
        self.cidade_entry = tk.Entry(self.form_frame)
        self.cidade_entry.grid(row=8, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.form_frame, text="E-mail:", bg="#d0f0c0")
        self.email_label.grid(row=8, column=2, sticky="e", padx=5, pady=5)
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=8, column=3, padx=5, pady=5)

        # Formulário de Envio de e-mail para cobrança
        self.email_envio_label = tk.Label(self.form_frame, text="E-mail para Envio de Cobrança:", bg="#d0f0c0")
        self.email_envio_label.grid(row=9, column=0, sticky="e", padx=5, pady=5)
        self.email_envio_entry = tk.Entry(self.form_frame)
        self.email_envio_entry.grid(row=9, column=1, padx=5, pady=5)

        # Caixa de Seleção para Inativo
        self.inativo_var = tk.IntVar()
        self.inativo_check = tk.Checkbutton(self.form_frame, text="Cliente Inativo", variable=self.inativo_var, bg="#d0f0c0")
        self.inativo_check.grid(row=9, column=2, columnspan=4, padx=5, pady=5)

        # Novos campos adicionados
        # Caixa de seleção para alertar sobre contas vencidas
        self.alertar_vencido_var = tk.IntVar()
        self.alertar_vencido_check = tk.Checkbutton(self.form_frame, text="Alertar sobre Contas Vencidas", variable=self.alertar_vencido_var, bg="#d0f0c0")
        self.alertar_vencido_check.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        # Formas de pagamento
        self.pagamento_label = tk.Label(self.form_frame, text="Formas de Pagamento:", bg="#d0f0c0")
        self.pagamento_label.grid(row=10, column=2, sticky="e", padx=5, pady=5)
        self.pagamento_entry = tk.Entry(self.form_frame)
        self.pagamento_entry.grid(row=10, column=3, padx=5, pady=5)

        # Transportadora
        self.transportadora_label = tk.Label(self.form_frame, text="Transportadora:", bg="#d0f0c0")
        self.transportadora_label.grid(row=11, column=0, sticky="e", padx=5, pady=5)
        self.transportadora_entry = tk.Entry(self.form_frame)
        self.transportadora_entry.grid(row=11, column=1, padx=5, pady=5)

        # Tabela de preços
        self.tabela_label = tk.Label(self.form_frame, text="Tabela de Preços:", bg="#d0f0c0")
        self.tabela_label.grid(row=11, column=2, sticky="e", padx=5, pady=5)
        self.tabela_entry = tk.Entry(self.form_frame)
        self.tabela_entry.grid(row=11, column=3, padx=5, pady=5)

        # Grupo de Cliente
        self.grupo_label = tk.Label(self.form_frame, text="Grupo de Cliente:", bg="#d0f0c0")
        self.grupo_label.grid(row=11, column=4, sticky="e", padx=5, pady=5)
        self.grupo_entry = tk.Entry(self.form_frame)
        self.grupo_entry.grid(row=11, column=5, padx=5, pady=5)

        # Venda bloqueada
        self.venda_bloqueada_var = tk.IntVar()
        self.venda_bloqueada_check = tk.Checkbutton(self.form_frame, text="Venda Bloqueada", variable=self.venda_bloqueada_var, bg="#d0f0c0")
        self.venda_bloqueada_check.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

        # Cliente inativo
        self.cliente_inativo_var = tk.IntVar()
        self.cliente_inativo_check = tk.Checkbutton(self.form_frame, text="Cliente Inativo", variable=self.cliente_inativo_var, bg="#d0f0c0")
        self.cliente_inativo_check.grid(row=12, column=2, columnspan=4, padx=5, pady=5)

        # Observações de alerta na venda
        self.observacao_alerta_label = tk.Label(self.form_frame, text="Observações Alerta na Venda:", bg="#d0f0c0")
        self.observacao_alerta_label.grid(row=13, column=0, sticky="e", padx=5, pady=5)
        self.observacao_alerta_entry = tk.Entry(self.form_frame)
        self.observacao_alerta_entry.grid(row=13, column=1, padx=5, pady=5)

        # Observações diversas
        self.observacao_diversas_label = tk.Label(self.form_frame, text="Observações Diversas:", bg="#d0f0c0")
        self.observacao_diversas_label.grid(row=13, column=2, sticky="e", padx=5, pady=5)
        self.observacao_diversas_entry = tk.Entry(self.form_frame)
        self.observacao_diversas_entry.grid(row=13, column=3, padx=5, pady=5)

        # ICMS Interno próprio
        self.icms_interno_label = tk.Label(self.form_frame, text="ICMS Interno Próprio:", bg="#d0f0c0")
        self.icms_interno_label.grid(row=13, column=4, sticky="e", padx=5, pady=5)
        self.icms_interno_entry = tk.Entry(self.form_frame)
        self.icms_interno_entry.grid(row=13, column=5, padx=5, pady=5)

        # Inscrição Suframa
        self.inscricao_suframa_label = tk.Label(self.form_frame, text="Inscrição Suframa:", bg="#d0f0c0")
        self.inscricao_suframa_label.grid(row=14, column=0, sticky="e", padx=5, pady=5)
        self.inscricao_suframa_entry = tk.Entry(self.form_frame)
        self.inscricao_suframa_entry.grid(row=14, column=1, padx=5, pady=5)

        # Data do cadastro
        self.data_cadastro_label = tk.Label(self.form_frame, text="Data Cadastro:", bg="#d0f0c0")
        self.data_cadastro_label.grid(row=14, column=2, sticky="e", padx=5, pady=5)
        self.data_cadastro_entry = tk.Entry(self.form_frame)
        self.data_cadastro_entry.grid(row=14, column=3, padx=5, pady=5)

        # Data última alteração
        self.data_ultima_alteracao_label = tk.Label(self.form_frame, text="Data Última Alteração:", bg="#d0f0c0")
        self.data_ultima_alteracao_label.grid(row=14, column=4, sticky="e", padx=5, pady=5)
        self.data_ultima_alteracao_entry = tk.Entry(self.form_frame)
        self.data_ultima_alteracao_entry.grid(row=14, column=5, padx=5, pady=5)

        # Cadastrado por
        self.cadastrado_por_label = tk.Label(self.form_frame, text="Cadastrado/Alterado por:", bg="#d0f0c0")
        self.cadastrado_por_label.grid(row=15, column=0, sticky="e", padx=5, pady=5)
        self.cadastrado_por_entry = tk.Entry(self.form_frame)
        self.cadastrado_por_entry.grid(row=15, column=1, padx=5, pady=5)

        # Botão para salvar as informações
        self.save_button = tk.Button(master, text="Salvar", command=self.save_client_data)
        self.save_button.pack(pady=10)

    def save_client_data(self):
        # Coleta os dados dos campos
        client_data = {
            "CPF/CNPJ": self.cpf_entry.get(),
            "Nome": self.name_entry.get(),
            "Razão Social": self.razao_entry.get(),
            "Contato": self.contato_entry.get(),
            "Telefone": self.telefone_entry.get(),
            "Celular": self.celular_entry.get(),
            "Fax": self.fax_entry.get(),
            "Data Nascimento": self.data_nasc_entry.get(),
            "Sexo": self.sexo_var.get(),
            "Inscrição Estadual": self.inscricao_estadual_entry.get(),
            "Documento": self.doc_entry.get(),
            "Categoria": self.categoria_entry.get(),
            "Endereço": self.endereco_entry.get(),
            "Número": self.numero_entry.get(),
            "Complemento": self.complemento_entry.get(),
            "Bairro": self.bairro_entry.get(),
            "Estado": self.estado_entry.get(),
            "Cidade": self.cidade_entry.get(),
            "E-mail": self.email_entry.get(),
            "E-mail para Envio de Cobrança": self.email_envio_entry.get(),
            "Observações Alerta na Venda": self.observacao_alerta_entry.get(),
            "Observações Diversas": self.observacao_diversas_entry.get(),
            "ICMS Interno": self.icms_interno_entry.get(),
            "Inscrição Suframa": self.inscricao_suframa_entry.get(),
            "Data Cadastro": self.data_cadastro_entry.get(),
            "Data Última Alteração": self.data_ultima_alteracao_entry.get(),
            "Cadastrado Por": self.cadastrado_por_entry.get()
        }

        # Exibe as informações em um messagebox
        messagebox.showinfo("Dados do Cliente", str(client_data))

# Criação da interface gráfica
root = tk.Tk()
client_form = ClientForm(root)
root.mainloop()
