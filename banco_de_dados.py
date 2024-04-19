import pyodbc
from tkinter import messagebox
import datetime


class Dados:
    def __init__(self):
        self.dados_De_conexao = None
        self.conexao = None
        self.command = None
        self.conectar()

    def conectar(self):
        try:
            self.dados_De_conexao = (
                "Driver={SQL server};"
                "Server=DESKTOP-NSKNLOB;"
                "Database=Biblioteca;"
            )
            self.conexao = pyodbc.connect(self.dados_De_conexao)
            return self.conexao

        except pyodbc.OperationalError as e:
            messagebox.showerror("Erro", f"Não foi Possivel conectar ao servidor {e}")
            return

    def adicionar_livros(self, nome, autor, genero, estante, prateleira, quantidade):
        try:

            if not nome or not autor or not genero or not estante or not prateleira or not quantidade:
                messagebox.showerror("ERRO", "Preencha todos os campos")
                return

            else:
                self.command = f"""INSERT INTO Livros (Nome, Autor, Genero, Estante, Prateleira, Quantidade)
                            VALUES
                                   ('{nome}', '{autor}', '{genero}', '{estante}','{prateleira}',{quantidade})"""
                self.rodar_comandos_add(self.command)
                messagebox.showinfo("Adicionado com sucesso")
        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

    def adicionar_alunos(self, nome, serie, turma, sala, endereco):
        try:
            if int(sala):
                sala = int(sala)
            else:
                return
            if not nome or not serie or not turma or not sala or not endereco:
                messagebox.showerror("ERRO", "Preencha todos os campos")
                return
            else:
                self.command = f"""INSERT INTO Aluno (Nome, Serie, Turma, Sala, Endereco, ADM)
                                    VALUES
                                   ('{nome}', '{serie}', '{turma}', {sala},'{endereco}','NOT')"""
                self.rodar_comandos_add(self.command)
        except pyodbc.Error as e:
            messagebox.showerror("ERRO", f"{e}")
        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

    def emprestar_livro(self, nome, serie, turma, sala, livro):

        try:
            self.command = f"""SELECT * FROM Aluno WHERE Nome = '{nome}'AND Serie = '{serie}' AND Turma = '{turma}'
            AND Sala = '{sala}' ORDER BY ID"""

            dados = self.verificar_dados(self.command)

            if dados:
                data = datetime.datetime.now()
                data.strftime("%d-%m-%Y")
                data_devolucao = data + datetime.timedelta(weeks=1)
                command = f"""INSERT INTO Emprestimo (Aluno,Namelivro, Serie, Turma, Sala, Dataemprestimo, Datadevolucao)
                                    VALUES
                             ('{nome}', '{livro}', '{serie}', {turma},'{sala}','{data}', {data_devolucao})"""
                self.rodar_comandos_add(command)
                messagebox.showinfo("!!!", "concluido")
            else:
                messagebox.showerror("ERRO", f"error")
                return

        except pyodbc.Error as e:
            messagebox.showerror("ERRO", f"{e}")
        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

    def rodar_comandos_add(self, command):
        try:
            conn = self.conexao
            cursor = conn.cursor()
            cursor.execute(command)
            conn.commit()

        except pyodbc.Error as e:
            messagebox.showerror("ERRO", f"{e}")
        except Exception as e:
            messagebox.showerror("ERRO", f"{e}")

    def verificar_dados(self, command):
        try:
            conn = self.conexao
            cursor = conn.cursor()
            cursor.execute(command)
            dados = cursor.fetchall()
            return dados
        except pyodbc.Error as e:
            messagebox.showerror("ERRO", f"{e}")
