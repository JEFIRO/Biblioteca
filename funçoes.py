from tkinter import messagebox
from banco_de_dados import Dados
import datetime



class Funcoes:
    def __init__(self):
        self.banco_de_dados = Dados()
        self.lista_dados = None

    # Livros

    def adicionar_livros(self, dados, treeviwer):
        try:
            dado = (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
            print(dados)
            print(dado)
            self.banco_de_dados.adicionar_livros(dado)

            self.adicionar_dados_tv('SELECT * FROM Livros', treeviwer)

        except Exception as e:
            messagebox.showerror("ERRO", f"funcoes{e}")

    # Alunos

    def adicionar_aluno(self, dados, treeviwer):
        try:
            print(dados)
            alunos = (dados[0], dados[1], dados[2], dados[3], dados[4])
            print(alunos)
            self.banco_de_dados.adicionar_alunos(alunos)

            self.adicionar_dados_tv('SELECT * FROM Aluno', treeviwer)

        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")
            return

    # Emprestar

    def emprestar_add(self):
        try:
            if not self.lista_dados:
                messagebox.showerror("Erro", "Adicione os dados")
            else:

                #verificar = self.banco_de_dados.esta_disponivel(comand[0])

                nome = self.lista_dados[1]
                livro = self.lista_dados[0]
                serie = self.lista_dados[2]
                turma = self.lista_dados[3]
                endereco = self.lista_dados[4]
                data = self.lista_dados[5]
                data_dev = self.lista_dados[6]

                command = f"""INSERT INTO Emprestimo (Aluno, Namelivro, Serie, Turma, Dataemprestimo, Datadevolucao, devolvido, Endereço)
                                                    VALUES
                                             ('{nome}', '{livro}', '{serie}', '{turma}','{data_dev}','{data}', 'NOT', '{endereco}')"""

                self.banco_de_dados.rodar_comandos_add(command)

        except Exception as e:
            messagebox.showerror("Erro", f"{e}")
            return

    def adicionar_dados_tv_emprestar(self, dados, dados2, tree):
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
                tree.delete(*tree.get_children())

                # Converter os itens da lista para strings


                # Inserir os dados na treeview
                tree.insert("", "end", values=self.lista_dados)

        except IndexError:
            pass
    # Geral

    def adicionar_dados_tv(self, comando, treeview):
        try:
            dados = self.banco_de_dados.verificar_dados(comando)
            treeview.delete(*treeview.get_children())
            for livros in dados:
                item_cleaned = [str(x) for x in livros]
                treeview.insert("", "end", values=item_cleaned)
        except Exception as e:
            messagebox.showerror("ERROR", "e")