from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from banco_de_dados import Dados


class MinhaApp:
    def __init__(self):
        self.banco_de_dados = Dados()
        self.janela = Tk()
        self.janela.title("Biblioteca")
        self.janela.geometry('1360x768')
        self.preto = 'black'
        self.frames()
        self.livros()


        self.janela.mainloop()

    def frames(self):
        self.frame_tv = Frame(self.janela, bg=self.preto, width=850, height=550)
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
        comand = 'SELECT * FROM Livros'
        dados = self.banco_de_dados.verificar_dados(comand)
        self.treeview_livros.delete(*self.treeview_livros.get_children())
        for livros in dados:
            item_cleaned = [str(x) for x in livros]
            self.treeview_livros.insert("", "end", values=item_cleaned)


        # Scroll = ttk.Scrollbar(self.frame_tv, orient="horizontal", command=self.treeview.yview)
        # Scroll.grid(row=1, column=0, padx=10)
        # self.treeview.config(yscrollcommand=Scroll.set)
        self.dados_livros()

    def aluno(self):

        self.treeview_aluno = ttk.Treeview(self.frame_tv_aluno, columns=("nome", "serie", "turma", "sala", "endereco"), show="headings")

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

        self.treeview_aluno.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
    def dados_livros(self):
        # label
        try:
            self.label_nome = Label(self.frame_butao, text="Nome")
            self.label_nome.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_name = Entry(self.frame_butao)
            self.entry_name.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_autor = Label(self.frame_butao, text="Autor")
            self.label_autor.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_autor = Entry(self.frame_butao)
            self.entry_autor.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_genero = Label(self.frame_butao, text="Genero")
            self.label_genero.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_genero = Entry(self.frame_butao)
            self.entry_genero.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_estante = Label(self.frame_butao, text="Estante")
            self.label_estante.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_estante = Entry(self.frame_butao)
            self.entry_estante.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_prateleira = Label(self.frame_butao, text="Prateleira")
            self.label_prateleira.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_prateleira = Entry(self.frame_butao)
            self.entry_prateleira.pack(side='left', anchor='w', padx=10, pady=10)

            self.label_quantidade = Label(self.frame_butao, text="Quantidade")
            self.label_quantidade.pack(side='left', anchor='w', padx=10, pady=10)

            self.entry_quantidade = Entry(self.frame_butao)
            self.entry_quantidade.pack(side='left', anchor='w', padx=10, pady=10)

            self.adicionar_dados = Button(self.frame_butao, text='Adicionar',command=self.adicionar_livros)
            self.adicionar_dados.pack(side='left', anchor='w', padx=10, pady=10)
        except EXCEPTION as e:
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
        except EXCEPTION as e:
            messagebox.showerror("ERRO", f"{e}")

run = MinhaApp()
