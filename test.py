from banco_de_dados import Dados


def add_manual():
    livros = [
        ("Dom Quixote", "Miguel de Cervantes", "Romance", 1, 'A', 8),
        ("1984", "George Orwell", "Ficção Científica", 2, 'B', 5),
        ("Orgulho e Preconceito", "Jane Austen", "Romance Clássico", 3, 'C', 6),
        ("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 4, 'D', 7),
        ("Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico", 5, 'E', 4),
        ("Crime e Castigo", "Fiódor Dostoiévski", "Romance Psicológico", 6, 'F', 3),
        ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 7, 'A', 9),
        ("A Revolução dos Bichos", "George Orwell", "Ficção Política", 8, 'B', 4),
        ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Literatura Infantojuvenil", 9, 'C', 10),
        ("O Grande Gatsby", "F. Scott Fitzgerald", "Romance", 10, 'D', 6),
        ("A Arte da Guerra", "Sun Tzu", "Filosofia Militar", 11, 'E', 5),
        ("A Metamorfose", "Franz Kafka", "Ficção Absurda", 12, 'F', 7),
        ("O Hobbit", "J.R.R. Tolkien", "Fantasia", 13, 'A', 6),
        ("Anna Karenina", "Liev Tolstói", "Romance", 14, 'B', 8),
        ("Ulisses", "James Joyce", "Modernismo", 15, 'C', 4),
        ("O Morro dos Ventos Uivantes", "Emily Brontë", "Romance Gótico", 16, 'D', 6),
        ("Moby Dick", "Herman Melville", "Aventura", 17, 'E', 3),
        ("O Apanhador no Campo de Centeio", "J.D. Salinger", "Ficção", 18, 'F', 6),
        ("O Retrato de Dorian Gray", "Oscar Wilde", "Gótico", 19, 'A', 7),
        ("O Sol é para Todos", "Harper Lee", "Ficção", 20, 'B', 5),
        ("As Crônicas de Nárnia", "C.S. Lewis", "Fantasia", 1, 'C', 9),
        ("A Revolta de Atlas", "Ayn Rand", "Romance Filosófico", 2, 'D', 4),
        ("O Nome do Vento", "Patrick Rothfuss", "Fantasia", 3, 'E', 8),
        ("O Código Da Vinci", "Dan Brown", "Suspense", 4, 'F', 3),
        ("A Ilíada", "Homero", "Épico", 5, 'A', 5),
        ("A Odisséia", "Homero", "Épico", 6, 'B', 6),
        ("O Estrangeiro", "Albert Camus", "Filosofia Existencialista", 7, 'C', 7),
        ("O Leão, a Feiticeira e o Guarda-Roupa", "C.S. Lewis", "Fantasia", 8, 'D', 8),
        ("O Cão dos Baskervilles", "Arthur Conan Doyle", "Mistério", 9, 'E', 9),
        ("O Conde de Monte Cristo", "Alexandre Dumas", "Aventura", 10, 'F', 5),
        ("A Sangue Frio", "Truman Capote", "Romance Criminal", 11, 'A', 6),
        ("O Processo", "Franz Kafka", "Ficção Filosófica", 12, 'B', 7),
        ("O Labirinto dos Espíritos", "Carlos Ruiz Zafón", "Mistério", 13, 'C', 8),
        ("O Vermelho e o Negro", "Stendhal", "Romance", 14, 'D', 9),
        ("O Lobo do Mar", "Jack London", "Aventura", 15, 'E', 10),
        ("A Divina Comédia", "Dante Alighieri", "Épico", 16, 'F', 6),
        ("Os Irmãos Karamazov", "Fiódor Dostoiévski", "Filosofia", 17, 'A', 8),
        ("O Conquistador", "William Faulkner", "Romance", 18, 'B', 7),
        ("As Vinhas da Ira", "John Steinbeck", "Romance Social", 19, 'C', 6),
        ("O Velho e o Mar", "Ernest Hemingway", "Ficção", 20, 'D', 5),
        ("Grande Sertão: Veredas", "João Guimarães Rosa", "Ficção", 1, 'E', 10),
        ("O Médico e o Monstro", "Robert Louis Stevenson", "Gótico", 2, 'F', 11),
        ("A Revolta de Atlas", "Ayn Rand", "Romance Filosófico", 3, 'A', 9),
        ("A Sangue Frio", "Truman Capote", "Romance Criminal", 4, 'B', 8),
        ("O Retrato de Dorian Gray", "Oscar Wilde", "Gótico", 5, 'C', 7),
        ("O Estrangeiro", "Albert Camus", "Filosofia Existencialista", 6, 'D', 6),
        ("A Metamorfose", "Franz Kafka", "Ficção Absurda", 7, 'E', 5),
        ("O Apanhador no Campo de Centeio", "J.D. Salinger", "Ficção", 8, 'F', 4),
        ("O Cão dos Baskervilles", "Arthur Conan Doyle", "Mistério", 9, 'A', 3),
        ("O Conde de Monte Cristo", "Alexandre Dumas", "Aventura", 10, 'B', 2),
        ("O Sol é para Todos", "Harper Lee", "Ficção", 11, 'C', 1),
        ("O Grande Gatsby", "F. Scott Fitzgerald", "Romance", 12, 'D', 2),
        ("O Código Da Vinci", "Dan Brown", "Suspense", 13, 'E', 3),
        ("A Arte da Guerra", "Sun Tzu", "Filosofia Militar", 14, 'F', 4),
        ("A Metamorfose", "Franz Kafka", "Ficção Absurda", 15, 'A', 5),
        ("O Hobbit", "J.R.R. Tolkien", "Fantasia", 16, 'B', 6),
        ("Anna Karenina", "Liev Tolstói", "Romance", 17, 'C', 7),
        ("Ulisses", "James Joyce", "Modernismo", 18, 'D', 8),
        ("O Morro dos Ventos Uivantes", "Emily Brontë", "Romance Gótico", 19, 'E', 9),
        ("Moby Dick", "Herman Melville", "Aventura", 20, 'F', 10),
        ("A Guerra dos Tronos", "George R.R. Martin", "Fantasia", 1, 'A', 10),
        ("A Fúria dos Reis", "George R.R. Martin", "Fantasia", 2, 'A', 9),
        ("A Tormenta de Espadas", "George R.R. Martin", "Fantasia", 3, 'A', 8),
        ("O Festim dos Corvos", "George R.R. Martin", "Fantasia", 4, 'A', 7),
        ("A Dança dos Dragões", "George R.R. Martin", "Fantasia", 5, 'A', 6),
        ("Os Ventos do Inverno", "George R.R. Martin", "Fantasia", 6, 'A', 5),
        ("Um Sonho de Primavera", "George R.R. Martin", "Fantasia", 7, 'A', 4),
        ("Fogo & Sangue", "George R.R. Martin", "História Fictícia", 8, 'B', 8),
        ("A Princesa e a Rainha", "George R.R. Martin", "História Fictícia", 9, 'B', 7),
        ("O Príncipe de Westeros e Outras Histórias", "George R.R. Martin", "História Fictícia", 10, 'B', 6),
        ("Os Filhos do Dragão", "George R.R. Martin", "História Fictícia", 11, 'B', 5)


    ]
    for livro in livros:

        nome = livro[0]
        autor = livro[1]
        genero = livro[2]
        estante = livro[3]
        prateleira = livro[4]
        quantidade = livro[5]

        print(nome)



dados = add_manual()
