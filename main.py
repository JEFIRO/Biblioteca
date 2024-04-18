from tkinter import *
class MinhaApp:
    def __init__(self, janela):
        self.janela = janela
        self.preto = 'black'
        self.frame_login()
        self.frame_aluno()
        self.frame_butons()
        self.janela.mainloop()

    def frame_login(self):
        self.frame_tv = Frame(self.janela, bg=self.preto, width=900, height=550)
        self.frame_tv.grid(column=1, row=0, padx=0, pady=0, sticky="nsew")  # Posicionando à direita

    def frame_aluno(self):
        self.frame_tv_aluno = Frame(self.janela, bg='red', width=460, height=550)
        self.frame_tv_aluno.grid(column=0, row=0, padx=0, pady=0, sticky="nsew")  # Posicionando à esquerda

    def frame_butons(self):
        self.frame_butao = Frame(self.janela, bg='blue', width=90, height=218)
        self.frame_butao.grid(column=0, row=1, padx=0, pady=0, columnspan=2, sticky="nsew")  # Posicionando abaixo, estendendo por duas colunas

if __name__ == "__main__":
    root = Tk()
    app = MinhaApp(root)
