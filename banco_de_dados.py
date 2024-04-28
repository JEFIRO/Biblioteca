import pyodbc
from tkinter import messagebox
import datetime


class Dados:
    def __init__(self):
        self.dados_De_conexao = None
        self.conexao = None
        self.command = None
        self.conectar()
        #self.add_manual()

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

    def adicionar_livros(self, dado):
        try:

            nome = dado[0].capitalize()
            autor = dado[1].capitalize()
            genero = dado[2].capitalize()
            estante = dado[3]
            prateleira = dado[4].capitalize()
            quantidade = dado[5]

            if not nome or not autor or not genero or not estante or not prateleira or not quantidade:
                messagebox.showerror("ERRO", "Preencha todos os campos")
                return

            else:
                self.command = f"""INSERT INTO Livros (Nome, Autor, Genero, Estante, Prateleira, Quantidade)
                            VALUES
                                   ('{nome}', '{autor}', '{genero}', '{estante}','{prateleira}',{quantidade})"""
                self.rodar_comandos_add(self.command)

        except Exception as e:
            messagebox.showerror("ERRO", f"eu {e}")

    def adicionar_alunos(self, aluno):
        try:
            nome = aluno[0]
            serie = aluno[1]
            turma = aluno[2]
            sala = aluno[3]
            endereco = aluno[4]

            if not nome or not serie or not turma or not sala or not endereco:
                messagebox.showerror("ERRO", "Preencha todos os campos")
                return

            self.command = f"""INSERT INTO Aluno (Nome, Serie, Turma, Sala, Endereço, ADM, Senha)
                                VALUES
                               ('{nome}', '{serie}', '{turma}', {sala},'{endereco}','NOT', '')"""

            self.rodar_comandos_add(self.command)

        except pyodbc.Error as e:
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
            messagebox.showinfo("sucesso", "Adicionado com sucesso")

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

    def e_adm(self, dados):
        try:
            if not dados:
                messagebox.showerror("ERRO", f"preencha os campos")
                return

            else:

                nome = dados[0]
                senha = dados[1]

                comando = f"SELECT * FROM Aluno WHERE Senha = '{senha}'AND Nome = '{nome}' AND ADM = 'ADM';"

                verificar = self.verificar_dados(comando)

                return verificar

        except pyodbc.Error as e:
            messagebox.showerror("ERRO", f"{e}")

    def esta_disponivel(self, dados):
        try:
            if not dados:
                messagebox.showerror("ERRO", f"preencha os campos")
                return
            else:

                comando = f"SELECT Quantidade FROM Livros WHERE Nome = '{dados}';"
                print(dados)
                verificar = self.verificar_dados(comando)
                return verificar


        except pyodbc.Error as e :
            messagebox.showerror("ERRO", f"{e}")


    def add_manual(self):
        alunos = [
            ("João", "1", 'A', 10, "Rua A - 123", 'NOT'),
            ("Maria", "2", 'B', 15, "Rua B - 456", 'NOT'),
            ("Pedro", "3", 'C', 20, "Rua C - 789", 'NOT'),
            ("Ana", "1", 'D', 25, "Rua D - 1011", 'NOT'),
            ("Lucas", "2", 'E', 30, "Rua E - 1213", 'NOT'),
            ("Mariana", "3", 'F', 35, "Rua F - 1415", 'NOT'),
            ("Carlos", "1", 'A', 5, "Rua G - 1617", 'NOT'),
            ("Juliana", "2", 'B', 12, "Rua H - 1819", 'NOT'),
            ("Gabriel", "3", 'C', 18, "Rua I - 2021", 'NOT'),
            ("Luiza", "1", 'D', 22, "Rua J - 2223", 'NOT'),
            ("Rafael", "2", 'E', 27, "Rua K - 2425", 'NOT'),
            ("Fernanda", "3", 'F', 32, "Rua L - 2627", 'NOT'),
            ("Matheus", "1", 'A', 8, "Rua M - 2829", 'NOT'),
            ("Larissa", "2", 'B', 14, "Rua N - 3031", 'NOT'),
            ("Diego", "3", 'C', 19, "Rua O - 3233", 'NOT'),
            ("Amanda", "1", 'D', 24, "Rua P - 3435", 'NOT'),
            ("Vinícius", "2", 'E', 29, "Rua Q - 3637", 'NOT'),
            ("Camila", "3", 'F', 34, "Rua R - 3839", 'NOT'),
            ("Bruno", "1", 'A', 9, "Rua S - 4041", 'NOT'),
            ("Isabela", "2", 'B', 16, "Rua T - 4243", 'NOT'),
            ("Luciana", "1", 'C', 11, "Rua U - 4445", 'NOT'),
            ("Ricardo", "3", 'D', 28, "Rua V - 4647", 'NOT'),
            ("Beatriz", "2", 'E', 17, "Rua W - 4849", 'NOT'),
            ("Marcos", "1", 'F', 23, "Rua X - 5051", 'NOT'),
            ("Fernando", "3", 'A', 36, "Rua Y - 5253", 'NOT'),
            ("Carla", "2", 'B', 13, "Rua Z - 5455", 'NOT'),
            ("Jefferson Vitena", "2", "B", 11, "Rua Tres portoes, 130", "ADM"),
            ("Monique Marinho", "2", "B", 11, "Humildes, 130", "NOT")

        ]
        for aluno in alunos:
            self.adicionar_alunos(aluno)