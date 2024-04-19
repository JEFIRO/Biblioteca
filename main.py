from tkinter import *
from tkinter import ttk


class MinhaApp:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Biblioteca")
        self.janela.geometry('1300x700')
        self.preto = 'black'
        self.frames()
        self.livros()

        self.janela.mainloop()

    def frames(self):
        self.frame_tv = Frame(self.janela, bg=self.preto, width=850, height=550)
        self.frame_tv.grid(column=1, row=0, padx=0, pady=0, sticky="nsew")  # Posicionando à direita

        self.frame_tv_aluno = Frame(self.janela, bg='red', width=460, height=550)
        self.frame_tv_aluno.grid(column=0, row=0, padx=0, pady=0, sticky="nsew")  # Posicionando à esquerda

        self.frame_butao = Frame(self.janela, bg='blue', width=90, height=218)
        self.frame_butao.grid(column=0, row=1, padx=0, pady=0, columnspan=2, sticky="nsew")  # Posicionando abaixo, estendendo por duas colunas

    def livros(self):

        self.treeview = ttk.Treeview(self.frame_tv, columns=("nome", "autor", "genero", "estante", "prateleira",
                                                             "quantidade"),show="headings")
        self.treeview.heading("nome", text="Nome")
        self.treeview.heading("autor", text="Autor")
        self.treeview.heading("genero", text="Genero")
        self.treeview.heading("estante", text="Estante")
        self.treeview.heading("prateleira", text="Prateleira")
        self.treeview.heading("quantidade", text="Qt")

        self.treeview.column("nome", width=200)
        self.treeview.column("autor", width=150)
        self.treeview.column("genero", width=100)
        self.treeview.column("prateleira", width=60)
        self.treeview.column("quantidade", width=200)

        self.treeview.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

        # Scroll = ttk.Scrollbar(self.frame_tv, orient="horizontal", command=self.treeview.yview)
        # Scroll.grid(row=1, column=0, padx=10)
        # self.treeview.config(yscrollcommand=Scroll.set)


run = MinhaApp()