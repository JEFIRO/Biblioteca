from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

import pyodbc

from banco_de_dados import Dados


class MinhaApp:
    def __init__(self):
        self.lista_dados = None
        self.lista = ['',]
        self.lista_aluno = ['',]
        self.janela = Tk()
        self.janela.title("Biblioteca")
        self.janela.geometry('1050x568')
        self.preto = 'black'
        self.banco_de_dados = Dados()
        self.frames()
        self.livros()
        self.login()
        #self.aluno()
        self.emprestar()


        self.janela.mainloop()

    def login(self):

        login = Tk()
        login.title("Login")

        # nome
        label_nome = Label(login, text="USUARIO")
        label_nome.grid(row=0, column=0, padx=0, pady=10)

        entry_nome = Entry(login)
        entry_nome.grid(row=0, column=1, padx=0, pady=10)

        # senha
        label_senha = Label(login, text="SENHA")
        label_senha.grid(row=1, column=0, padx=10, pady=10)

        entry_senha = Entry(login)
        entry_senha.grid(row=1, column=1, padx=10, pady=10)

        button = Button(login, text="OK", width=10)
        button.grid(row=2, column=0, padx=10, pady=10)

    def frames(self):
        self.frame_tv = Frame(self.janela, bg=self.preto, width=900, height=550)
        self.frame_tv.pack(side="top", fill="both", expand=True)

        self.frame_butao = Frame(self.janela, bg='blue', width=90, height=218)
        self.frame_butao.pack(side="bottom", fill="x")

    def livros(self):

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
        self.adicionar_dados_tv('SELECT * FROM Livros', self.treeview_livros)
        self.bottao_livros()

        self.scrolbar(self.frame_tv, self.treeview_livros)

    def aluno(self):

        self.frame_aluno = Toplevel(self.frame_tv)

        self.treeview_aluno = ttk.Treeview(self.frame_aluno, columns=("nome", "serie", "turma", "sala", "endereco"), show="headings")

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

        self.adicionar_dados_tv('SELECT * FROM Aluno', self.treeview_aluno)

        self.bottao_alunos()

        self.scrolbar(self.frame_aluno, self.treeview_aluno)

    def emprestar(self):

        self.adicionar_a_lista()
        self.frame_emprestar = Toplevel(self.frame_tv)

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

        self.button_add = Button(self.frame_emprestar, text="Emprestar", command=lambda:self.enprestar_add(self.lista_dados))
        self.button_add.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    def enprestar_add(self, comand):
        try:
            if not self.lista_dados:
                messagebox.showerror("Erro","Adicine os dados")
            else:
                lista = "nome,livro, serie, turma, endereco, data_devolucao_formatada"
                print(comand)
                print(len(comand))
                nome = comand[1]
                livro = comand[0]
                serie = comand[2]
                turma = comand[3]
                endereco = comand[4]
                data = comand[5]
                data_dev = comand[6]

                command = f"""INSERT INTO Emprestimo (Aluno, Namelivro, Serie, Turma, Dataemprestimo, Datadevolucao, devolvido, Endereço)
                                                    VALUES
                                             ('{nome}', '{livro}', '{serie}', '{turma}','{data_dev}','{data}', 'NOT', '{endereco}')"""

                self.banco_de_dados.rodar_comandos_add(command)

        except Exception as e:
            messagebox.showerror("Erro", f"{e}")
            return

    def evento_clicar_botao(self, event):
        try:
            # Chamar os métodos para obter os dados necessários
            dados = self.item_selecionado()
            dados2 = self.item_selecionado_alunos()

            # Adicionar os dados à treeview
            self.adicionar_dados_tv_emprestar(dados, dados2[0])
        except IndexError:
            pass

        except Exception as e:
            messagebox.showerror("Erro", f"{e}")

    def item_selecionado_alunos(self, event=None):
        try:
            select = self.commonbox_aluno.get()

            command = f"SELECT Nome, Serie, Turma, Endereço FROM Aluno WHERE Nome = '{select}'"
            dados = self.banco_de_dados.verificar_dados(command)

            return dados

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

    def adicionar_dados_tv_emprestar(self, dados, dados2):
        try:
            # Verificar se os dados estão disponíveis antes de prosseguir

            if dados and dados2:
                # Extrair os dados do primeiro resultado (dados2) para o livro
                livro = dados[0][0]
                # Extrair os dados do segundo resultado (dados) para o aluno
                nome = dados2[0]  # Nome do aluno
                serie = dados2[1]  # Série do aluno
                turma = dados2[2]  # Turma do aluno
                endereco = dados2[3]  # Endereço do aluno

                # Calcular a data de devolução
                data_devolucao = datetime.datetime.now() + datetime.timedelta(weeks=1)
                data_devolucao_formatada = data_devolucao.strftime("%d/%m/%Y")
                data = datetime.datetime.now().strftime("%d/%m/%Y")
                # Criar a lista de dados a serem inseridos na treeview
                self.lista_dados = (livro, nome, serie, turma, endereco, data_devolucao_formatada, data)

                # Limpar a treeview antes de adicionar os novos dados
                self.treeview_emprestar.delete(*self.treeview_emprestar.get_children())

                # Converter os itens da lista para strings
                item_cleaned = [str(x) for x in self.lista_dados]

                # Inserir os dados na treeview
                self.treeview_emprestar.insert("", "end", values=item_cleaned)

        except IndexError:
            pass


    def atualizar_combobox(self, dados):
        var = dados[0]
        commonbox = dados[1]
        lista = dados[2]  # Corrigido para índice 2

        texto = var.get().lower()
        livros_correspondentes = [livro for livro in lista if texto in livro.lower()]
        commonbox['values'] = livros_correspondentes if texto else lista


    def abrir_menu(self, event ,commonbox):
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

            self.adicionar_dados = Button(self.frame_butao, text='Adicionar',command=self.adicionar_livros)
            self.adicionar_dados.pack(side='left', anchor='w', padx=10, pady=10)

            self.adicionar_aluno_tv = Button(self.frame_butao, text='Adicionar aluno', command=self.aluno)
            self.adicionar_aluno_tv.pack(side='left', anchor='w', padx=10, pady=10)


        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

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

            self.adicionar_dados_aluno = Button(self.frame_aluno, text='Adiciona', command=self.adicionar_aluno)
            self.adicionar_dados_aluno.pack(side='left', anchor='w', padx=10, pady=10)

        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

    def adicionar_livros(self):
        try:
            dados = [(self.entry_name.get(), self.entry_autor.get(), self.entry_genero.get(), self.entry_estante.get(),
                      self.entry_prateleira.get(), self.entry_quantidade.get())]
            print(dados)

            self.banco_de_dados.adicionar_livros(dados)

            self.adicionar_dados_tv('SELECT * FROM Livros', self.treeview_livros)

        except Exception as e:
            messagebox.showerror("ERRO", f"aqui{e}")


    def adicionar_aluno(self):
        try:
            alunos = (self.entry_name_aluno.get(), self.entry_serie_aluno.get(), self.entry_turma_aluno.get(),
                       self.entry_sala_aluno.get(), self.entry_endereco_aluno.get())

            self.banco_de_dados.adicionar_alunos(alunos)

            self.adicionar_dados_tv('SELECT * FROM Aluno', self.treeview_aluno)

        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")
            return

    def adicionar_dados_tv(self, comando, treeview):
        dados = self.banco_de_dados.verificar_dados(comando)
        treeview.delete(*treeview.get_children())
        for livros in dados:
            item_cleaned = [str(x) for x in livros]
            treeview.insert("", "end", values=item_cleaned)


    def scrolbar(self, frame, tree):

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y', anchor='n')
        tree.configure(yscrollcommand=scroll.set)

    def scroll_y(*args, text):
        text.yview(*args)


run = MinhaApp()
