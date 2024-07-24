package com.jefiro.Biblioteca.controler;

import com.jefiro.Biblioteca.modelos.*;
import com.jefiro.Biblioteca.repository.ClienteRepository;
import com.jefiro.Biblioteca.repository.EmprestimoRepository;
import com.jefiro.Biblioteca.repository.LivrosRepository;
import com.jefiro.Biblioteca.sevice.ApiService;
import com.jefiro.Biblioteca.sevice.ConverteDados;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class EmprestimoService {
    ApiService apiService = new ApiService();
    ConverteDados converteDados = new ConverteDados();
    List<VolumeInfo> livros = new ArrayList<>();
    @Autowired
    private LivrosRepository livroRepository;

    @Autowired
    private ClienteRepository clienteRepository;

    @Autowired
    private EmprestimoRepository emprestimoRepository;

    public List<Emprestimo> buscarEmprestimos() {
        return emprestimoRepository.findAll();
    }

    public List<Cliente> buscarClientes() {
        return clienteRepository.findAll();
    }

    public List<Livro> buscarLivros() {
        return livroRepository.findAll();
    }
    List<Livro> buncarLancamentos(){
        return livroRepository.findTop5ByOrderByDataDePublicacaoDesc();
    }
    List<Livro> buscarTop5(){
        return livroRepository.findTop5ByOrderByAvaliacaoDesc();
    }
    public void salvarLivro(Livro livro){
        try {
            livroRepository.save(livro);
        } catch (DataIntegrityViolationException e) {
            // Logar a exceção se necessário
            System.out.println("Tentativa de inserir um livro com dados duplicados ou violação de integridade: " + e.getMessage());
            // Você pode optar por não fazer nada ou lidar com a situação de outra forma
        } catch (Exception e) {
            // Captura outras exceções, se necessário
            System.out.println("Erro ao salvar o livro: " + e.getMessage());
        }
    }
    public List<Livro> buscarLivrosById(Long id) {
        Optional<Livro> livro = livroRepository.findById(id);
        if (livro.isPresent()){
            List<Livro> livros = new ArrayList<>();
            livros.add(livro.get());
            return livros;
        }
        return null;
    }

    public List<VolumeInfo> buscarLivros(String nomeLivro) {
        var json = apiService.querry(nomeLivro);
        Response response = converteDados.converteDados(json, Response.class);
        livros = response.items().stream().map(c -> new VolumeInfo(c.info().titulo(),
                c.info().autores(), c.info().descricao(), c.info().dataDePublicacao(), c.info().categoria(),
                c.info().avaliacao(), c.info().numeroDePaginas(), c.info().tipo(), c.info().Imgem())).collect(Collectors.toList());

        if (!livros.isEmpty()){
            livros.stream().map(v -> {
                Livro livro = new Livro(v);
                salvarLivro(livro);
                return livro;
            }).collect(Collectors.toList());
        }
        return livros;
    }

}
