package com.jefiro.Biblioteca.principal;

import com.jefiro.Biblioteca.modelos.*;
import com.jefiro.Biblioteca.repository.ClienteRepository;
import com.jefiro.Biblioteca.repository.EmprestimoRepository;
import com.jefiro.Biblioteca.repository.LivrosRepository;
import com.jefiro.Biblioteca.sevice.ApiService;
import com.jefiro.Biblioteca.sevice.ConverteDados;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Principal {
    Scanner leitura = new Scanner(System.in);
    ApiService apiService = new ApiService();
    ConverteDados converteDados = new ConverteDados();
    LivrosRepository repositoryLivros;
    ClienteRepository repositoryCliente;
    EmprestimoRepository repositoryEmprestimo;
    String json;

    public Principal(LivrosRepository repository, ClienteRepository repositoryCliente, EmprestimoRepository emprestimoRepository) {
        this.repositoryLivros = repository;
        this.repositoryCliente = repositoryCliente;
        this.repositoryEmprestimo = emprestimoRepository;
    }

    public void principal() {
        var menu = """
                1 - Buscar livros
                2 - Emprestar Livro
                3 - Cadastrar Clientes
                4 - Relatorio de emprestimo
                5 - Listar Livros
                6 - Clientes
                
                0 - sair
                """;
        int c = -1;
        while (c != 0) {
            System.out.println(menu);
            c = leitura.nextInt();
            leitura.nextLine();
            switch (c) {
                case 1:
                    buscarLivros();
                    break;
                case 2:
                    emprestarLivros();
                    break;
                case 3:
                    cadastrarCliente();
                    break;
                case 4 :
                    listaEmprestimos();
                    break;
                case 5:
                    listarLivros();
                    break;
                case 6:
                    listarClientes();
                    break;
                default:
                    System.out.println("Opção invalida!");
            }
        }
    }

    private void listaEmprestimos() {
        List<Emprestimo> emprestimoList =repositoryEmprestimo.findAll();
        emprestimoList.forEach(System.out::println);
    }

    private void cadastrarCliente() {
        System.out.println("Cadastro de Clientes");
        System.out.println("Nome: ");
        var nome = leitura.nextLine();
        System.out.println("Endereco: ");
        var endereco = leitura.nextLine();
        System.out.println("Contato: ");
        var contato = leitura.nextLine();
        Cliente cliente = new Cliente(nome,endereco,contato);
        repositoryCliente.save(cliente);


    }

    private void emprestarLivros() {
        listarLivros();
        System.out.println("digite o id do Livro");
        var livroId = leitura.nextLong();
        Optional<Livro> optionalLivro = repositoryLivros.findById(livroId);
        if (optionalLivro.isPresent()){
            listarClientes();
            System.out.println("digite o id do Livro");
            var clienteId = leitura.nextLong();
            Optional<Cliente> optionalCliente = repositoryCliente.findById(clienteId);
            if (optionalCliente.isPresent()){
                Emprestimo emprestimo = new Emprestimo();
                emprestimo.setLivros(List.of(optionalLivro.get()));
                emprestimo.setCliente(optionalCliente.get());
                emprestimo.setDataDeEmprestimo(LocalDate.now());
                emprestimo.setDataDeDevolucao(LocalDate.now().plusMonths(1));
                repositoryEmprestimo.save(emprestimo);
            }
        }
    }

    private void buscarLivros() {
        // pede o nome do livro
        System.out.println("Nome do livro: ");
        var nomeLivro = leitura.nextLine();
        var livroApi =buscarLivroApi(nomeLivro);
        // busca um livro especifico na lista
        System.out.println("escolha um livro: ");
        var livroEscolhido = leitura.nextLine();
        salvarLivros(livroEscolhido,livroApi);
    }

    private void listarLivros() {
        List<Livro> livro = repositoryLivros.findAll();
        livro.forEach(System.out::println);
    }

    private void listarClientes() {
        List<Cliente> cliente = repositoryCliente.findAll();
        cliente.forEach(System.out::println);
    }
    private List<VolumeInfo> buscarLivroApi(String nomeLivro){
        json = apiService.querry(nomeLivro);
        Response response = converteDados.converteDados(json, Response.class);
        List<VolumeInfo> livros = response.items().stream().map(c -> new VolumeInfo(c.info().titulo(),
                c.info().autores(), c.info().descricao(), c.info().dataDePublicacao(), c.info().categoria(),
                c.info().avaliacao(), c.info().numeroDePaginas(), c.info().tipo(),c.info().Imgem())).collect(Collectors.toList());
        livros.forEach(System.out::println);
        return livros;
    }
    private void salvarLivros(String nome, List<VolumeInfo> livros){
        livros.stream().filter(l -> l.titulo().equals(nome)).forEach(
                v -> {
                    repositoryLivros.save(new Livro(v));
                }
        );
    }

}
