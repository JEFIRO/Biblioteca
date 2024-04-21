from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from banco_de_dados import Dados


class MinhaApp:
    def __init__(self):
        self.lista = ['',]
        self.janela = Tk()
        self.janela.title("Biblioteca")
        self.janela.geometry('1050x568')
        self.preto = 'black'
        self.banco_de_dados = Dados()
        self.frames()
        self.livros()
        #self.aluno()
        self.emprestar()


        self.janela.mainloop()

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

    def atualizar_combobox(self):
        texto = self.commonbox_var.get().lower()
        livros_correspondentes = [livro for livro in self.lista if texto in livro.lower()]
        self.commonbox['values'] = livros_correspondentes if texto else self.lista

    def abrir_menu(self, event):
        self.commonbox.event_generate('<Down>')

    def emprestar(self):
        self.adicionar_a_lista()
        self.frame_emprestar = Toplevel(self.frame_tv)

        self.commonbox_var = StringVar()
        self.commonbox = ttk.Combobox(self.frame_emprestar, textvariable=self.commonbox_var)
        self.commonbox['values'] = self.lista
        self.commonbox.pack()

        self.commonbox.bind('<KeyRelease>', lambda event=None:  (self.atualizar_combobox(), self.abrir_menu(event)))


    def adicionar_a_lista(self):

        dados = self.banco_de_dados.verificar_dados('SELECT Nome FROM Livros')
        for dado in dados:
            item_cleaned = str(dado[0])  # Pega o primeiro elemento da tupla
            self.lista.append(item_cleaned)  # Adiciona à lista


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
            nome = self.entry_name.get()
            autor = self.entry_autor.get()
            genero = self.entry_genero.get()
            estante = self.entry_estante.get()
            prateleira = self.entry_prateleira.get()
            quantidade = self.entry_quantidade.get()

            self.banco_de_dados.adicionar_livros(nome, autor, genero, estante, prateleira, quantidade)
            self.adicionar_dados_tv('SELECT * FROM Livros', self.treeview_livros)

        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")


    def adicionar_aluno(self):
        try:
            nome = self.entry_name_aluno.get()
            serie = self.entry_serie_aluno.get()
            turma = self.entry_turma_aluno.get()
            sala = self.entry_sala_aluno.get()
            endereco = self.entry_endereco_aluno.get()

            self.banco_de_dados.adicionar_alunos(nome, serie, turma, sala, endereco)
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
