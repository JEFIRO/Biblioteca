package com.jefiro.Biblioteca.controler;

import com.jefiro.Biblioteca.modelos.*;
import com.jefiro.Biblioteca.repository.ClienteRepository;
import com.jefiro.Biblioteca.repository.EmprestimoRepository;
import com.jefiro.Biblioteca.repository.LivrosRepository;
import com.jefiro.Biblioteca.sevice.ApiService;
import com.jefiro.Biblioteca.sevice.ConverteDados;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class EmprestimoService {
    ApiService apiService = new ApiService();
    ConverteDados converteDados = new ConverteDados();
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
    public List<Livro> buscarLivrosById(Long id) {
        Optional<Livro> livro = livroRepository.findById(id);
        if (livro.isPresent()){
            List<Livro> livros = new ArrayList<>();
            livros.add(livro.get());
            return livros;
        }
        return null;
    }

    public List<VolumeInfo> c(String nomeLivro) {
        var json = apiService.querry(nomeLivro);
        Response response = converteDados.converteDados(json, Response.class);
        List<VolumeInfo> livros = response.items().stream().map(c -> new VolumeInfo(c.info().titulo(),
                c.info().autores(), c.info().descricao(), c.info().dataDePublicacao(), c.info().categoria(),
                c.info().avaliacao(), c.info().numeroDePaginas(), c.info().tipo(), c.info().Imgem())).collect(Collectors.toList());
        //livros.stream().forEach(v -> livroRepository.save(new Livro(v)));
        return livros;
    }
    public List<Livro> salvarLivroSelecionado(String nomeLivro){



    }

}
