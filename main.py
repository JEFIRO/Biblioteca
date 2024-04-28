from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc
from banco_de_dados import Dados
from funçoes import Funcoes


class MinhaApp:
    def __init__(self):
        self.lista = ['',]
        self.lista_aluno = ['',]

        self.banco_de_dados = Dados()
        self.funcao = Funcoes()

        self.login()
        self.logi.mainloop()

    # Login

    def login(self):

        self.logi = Tk()
        self.logi.title("Login")

        # nome
        self.label_nome_ADM = Label(self.logi, text="USUARIO")
        self.label_nome_ADM.grid(row=0, column=0, padx=0, pady=10)

        self.entry_nome_ADM = Entry(self.logi)
        self.entry_nome_ADM.grid(row=0, column=1, padx=0, pady=10)

        # senha
        self.label_senha_ADM = Label(self.logi, text="SENHA")
        self.label_senha_ADM.grid(row=1, column=0, padx=10, pady=10)

        self.entry_senha_ADM = Entry(self.logi, show="#")
        self.entry_senha_ADM.grid(row=1, column=1, padx=10, pady=10)

        button = Button(self.logi, text="OK", width=10, command=self.verifica)
        button.grid(row=2, column=0, padx=10, pady=10)

    def opcoes(self):

        self.logi.withdraw()

        self.opcoes_frame = Toplevel(self.logi)
        self.opcoes_frame.title("Opções")

        butao_livros = Button(self.opcoes_frame, text="Adicionar Livros", command=self.livros, width=20)
        butao_livros.grid(row=0, column=0, padx=20, pady=30)

        butao_aluno = Button(self.opcoes_frame, text="Adicionar Alunos", command=self.aluno, width=20)
        butao_aluno.grid(row=0, column=1, padx=5, pady=30)

        butao_emprestar = Button(self.opcoes_frame, text="Emprestar Livros", command=self.emprestar, width=20)
        butao_emprestar.grid(row=0, column=2, padx=20, pady=30)

    def verifica(self):
        comando = (self.entry_nome_ADM.get(), self.entry_senha_ADM.get())

        verificador = self.banco_de_dados.e_adm(comando)

        if verificador:
            self.opcoes()
        else:
            messagebox.showerror("ERRO", "Você não tem permição")

    # Emprestar

    def emprestar(self):

        self.adicionar_a_lista()
        self.frame_emprestar = Toplevel(self.opcoes_frame)

        self.treeview_emprestar = ttk.Treeview(self.frame_emprestar, columns=(
            "Nome do livro", "Nome", "Serie", "Turma", "Endereço", "Devolução"), show="headings")

        self.treeview_emprestar.heading("Nome do livro", text="Nome do livro")
        self.treeview_emprestar.heading("Nome", text="Nome")
        self.treeview_emprestar.heading("Serie", text="Série")
        self.treeview_emprestar.heading("Turma", text="Turma")
        self.treeview_emprestar.heading("Endereço", text="Endereço")
        self.treeview_emprestar.heading("Devolução", text="Devolução")

        self.treeview_emprestar.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        label_name = Label(self.frame_emprestar, text="Livro")
        label_name.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.commonbox_var = StringVar()
        self.commonbox = ttk.Combobox(self.frame_emprestar, textvariable=self.commonbox_var)
        self.commonbox.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.commonbox['values'] = self.lista
        dados = (self.commonbox_var, self.commonbox, self.lista)
        self.commonbox.bind('<KeyRelease>',
                            lambda event=None: (self.atualizar_combobox(dados), self.abrir_menu(event, self.commonbox)))
        self.commonbox.bind("<<ComboboxSelected>>", self.evento_clicar_botao)

        label_name_aluno = Label(self.frame_emprestar, text="Aluno")
        label_name_aluno.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.commonbox_var_aluno = StringVar()
        self.commonbox_aluno = ttk.Combobox(self.frame_emprestar, textvariable=self.commonbox_var_aluno)
        self.commonbox_aluno.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.commonbox_aluno['values'] = self.lista_aluno

        dados2 = (self.commonbox_var_aluno, self.commonbox_aluno, self.lista_aluno)

        self.commonbox_aluno.bind('<KeyRelease>', lambda event=None: (
        self.atualizar_combobox(dados2), self.abrir_menu(event, self.commonbox_aluno)))
        self.commonbox_aluno.bind("<<ComboboxSelected>>", self.evento_clicar_botao)

        self.button_add = Button(self.frame_emprestar, text="Emprestar", command=self.funcao.emprestar_add)
        self.button_add.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    def evento_clicar_botao(self, event):
        try:
            # Chamar os métodos para obter os dados necessários
            dados = self.item_selecionado()
            dados2 = self.item_selecionado_alunos()

            # Adicionar os dados à treeview
            self.funcao.adicionar_dados_tv_emprestar(dados, dados2[0], self.treeview_emprestar)

        except IndexError:
            pass

        except Exception as e:
            messagebox.showerror("Erro", f"{e}")

    def item_selecionado(self, event=None):
        try:
            select = self.commonbox.get()

            command = f"SELECT Nome FROM Livros WHERE Nome = '{select}'"
            dados = self.banco_de_dados.verificar_dados(command)
            return dados

        except Exception as e:
            messagebox.showerror("Erro", f"{e}")

    def abrir_menu(self, event,commonbox):
        commonbox.event_generate('<Down>')

    def adicionar_a_lista(self):
        try:
            dados = self.banco_de_dados.verificar_dados('SELECT Nome FROM Livros')
            for dado in dados:
                item_cleaned = str(dado[0])  # Pega o primeiro elemento da tupla
                self.lista.append(item_cleaned)  # Adiciona à lista

            dados = self.banco_de_dados.verificar_dados('SELECT Nome FROM Aluno')
            for dado in dados:
                item_cleaned = str(dado[0])  # Pega o primeiro elemento da tupla
                self.lista_aluno.append(item_cleaned)  # Adiciona à lista
        except pyodbc.Error as e:
            messagebox.showerror("Erro", f"{e}")

    # Livro

    def livros(self):
        livros = Toplevel(self.opcoes_frame)

        self.frame_tv = Frame(livros, bg="black", width=900, height=550)
        self.frame_tv.pack(side="top", fill="both", expand=True)

        self.frame_butao = Frame(livros, bg='blue', width=90, height=218)
        self.frame_butao.pack(side="bottom", fill="x")

        self.treeview_livros = ttk.Treeview(self.frame_tv, columns=("nome", "autor", "genero", "estante", "prateleira",
                                                             "quantidade"),show="headings")
        self.treeview_livros.heading("nome", text="Nome")
        self.treeview_livros.heading("autor", text="Autor")
        self.treeview_livros.heading("genero", text="Genero")
        self.treeview_livros.heading("estante", text="Estante")
        self.treeview_livros.heading("prateleira", text="Prateleira")
        self.treeview_livros.heading("quantidade", text="Qt")

        self.treeview_livros.column("nome", width=200)
        self.treeview_livros.column("autor", width=150)
        self.treeview_livros.column("genero", width=100)
        self.treeview_livros.column("prateleira", width=60)
        self.treeview_livros.column("quantidade", width=20)

        self.treeview_livros.pack(padx=10, pady=10)

        self.funcao.adicionar_dados_tv('SELECT * FROM Livros', self.treeview_livros)

        self.bottao_livros()

        self.scrolbar(self.frame_tv, self.treeview_livros)

    def bottao_livros(self):
        # label
        try:
            self.label_nome = Label(self.frame_butao, text="Nome")
            self.label_nome.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_name = Entry(self.frame_butao, width=10)
            self.entry_name.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_autor = Label(self.frame_butao, text="Autor")
            self.label_autor.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_autor = Entry(self.frame_butao, width=10)
            self.entry_autor.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_genero = Label(self.frame_butao, text="Genero")
            self.label_genero.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_genero = Entry(self.frame_butao, width=10)
            self.entry_genero.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_estante = Label(self.frame_butao, text="Estante")
            self.label_estante.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_estante = Entry(self.frame_butao, width=10)
            self.entry_estante.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_prateleira = Label(self.frame_butao, text="Prateleira")
            self.label_prateleira.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_prateleira = Entry(self.frame_butao, width=5)
            self.entry_prateleira.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_quantidade = Label(self.frame_butao, text="Quantidade")
            self.label_quantidade.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_quantidade = Entry(self.frame_butao, width=5)
            self.entry_quantidade.pack(side='left', anchor='w', padx=10, pady=10)

            self.adicionar_dados = Button(self.frame_butao, text='Adicionar',command=lambda: self.funcao.adicionar_livros(self.coletar_livros(), self.treeview_livros))
            self.adicionar_dados.pack(side='left', anchor='w', padx=10, pady=10)

            self.adicionar_aluno_tv = Button(self.frame_butao, text='Adicionar aluno', command=self.aluno)
            self.adicionar_aluno_tv.pack(side='left', anchor='w', padx=10, pady=10)

        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

    def coletar_livros(self):

        dados = (self.entry_name.get(), self.entry_autor.get(), self.entry_genero.get(), self.entry_estante.get(),
                 self.entry_prateleira.get(), self.entry_quantidade.get())
        return dados

    # Aluno

    def aluno(self):

        self.frame_aluno = Toplevel(self.opcoes_frame)

        self.treeview_aluno = ttk.Treeview(self.frame_aluno, columns=("nome", "serie", "turma", "sala", "endereco"),
                                           show="headings")

        self.treeview_aluno.heading("nome", text="Nome")
        self.treeview_aluno.heading("serie", text="Serie")
        self.treeview_aluno.heading("turma", text="Turma")
        self.treeview_aluno.heading("sala", text="Sala")
        self.treeview_aluno.heading("endereco", text="Endereço")

        self.treeview_aluno.column("nome", width=200)
        self.treeview_aluno.column("serie", width=60)
        self.treeview_aluno.column("turma", width=60)
        self.treeview_aluno.column("sala", width=60)
        self.treeview_aluno.column("endereco", width=100)

        self.treeview_aluno.pack(padx=10, pady=10)

        self.funcao.adicionar_dados_tv('SELECT * FROM Aluno', self.treeview_aluno)

        self.bottao_alunos()

        self.scrolbar(self.frame_aluno, self.treeview_aluno)

    def bottao_alunos(self):
        try:
            self.label_nome_aluno = Label(self.frame_aluno, text="Nome")
            self.label_nome_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_name_aluno = Entry(self.frame_aluno, width=10)
            self.entry_name_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_serie_aluno = Label(self.frame_aluno, text="serie")
            self.label_serie_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_serie_aluno = Entry(self.frame_aluno, width=10)
            self.entry_serie_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_turma_aluno = Label(self.frame_aluno, text="turma")
            self.label_turma_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_turma_aluno = Entry(self.frame_aluno, width=10)
            self.entry_turma_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_sala_aluno = Label(self.frame_aluno, text="sala")
            self.label_sala_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_sala_aluno = Entry(self.frame_aluno, width=10)
            self.entry_sala_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_endereco_aluno = Label(self.frame_aluno, text="endereco")
            self.label_endereco_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_endereco_aluno = Entry(self.frame_aluno, width=5)
            self.entry_endereco_aluno.pack(side='left', anchor='w', padx=10, pady=10)

            self.adicionar_dados_aluno = Button(self.frame_aluno, text='Adiciona', command=lambda: self.funcao.adicionar_aluno(self.coletar(), self.treeview_aluno))
            self.adicionar_dados_aluno.pack(side='left', anchor='w', padx=10, pady=10)

        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

    def coletar(self):
        dados = (self.entry_name_aluno.get(), self.entry_serie_aluno.get(), self.entry_turma_aluno.get(),
                 self.entry_sala_aluno.get(), self.entry_endereco_aluno.get())
        self.adicionar_a_lista()
        return dados

    def item_selecionado_alunos(self, event=None):
        try:
            select = self.commonbox_aluno.get()

            command = f"SELECT Nome, Serie, Turma, Endereço FROM Aluno WHERE Nome = '{select}'"
            dados = self.banco_de_dados.verificar_dados(command)

            return dados

        except Exception as e:
            messagebox.showerror("Erro", f"{e}")

    # Geral

    def atualizar_combobox(self, dados):

        var = dados[0]
        commonbox = dados[1]
        lista = dados[2]  # Corrigido para índice 2

        texto = var.get().lower()
        livros_correspondentes = [livro for livro in lista if texto in livro.lower()]
        commonbox['values'] = livros_correspondentes if texto else lista

    def scrolbar(self, frame, tree):

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y', anchor='n')
        tree.configure(yscrollcommand=scroll.set)

    def scroll_y(*args, text):
        text.yview(*args)


run = MinhaApp()
