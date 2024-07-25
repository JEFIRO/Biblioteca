package com.jefiro.Biblioteca.controler;

import com.jefiro.Biblioteca.modelos.*;
import com.jefiro.Biblioteca.modelos.dto.EmprestimoDTO;
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

    @Autowired
    private LivrosRepository livroRepository;

    @Autowired
    private ClienteRepository clienteRepository;

    @Autowired
    private EmprestimoRepository emprestimoRepository;


    public List<Livro> buscarLivros() {
        return livroRepository.findAll();
    }


    public List<Livro> buscarLivrosById(Long id) {
        Optional<Livro> livro = livroRepository.findById(id);
        if (livro.isPresent()) {
            List<Livro> livros = new ArrayList<>();
            livros.add(livro.get());
            return livros;
        }
        return null;
    }

    public List<VolumeInfo> buscarLivros(String nomeLivro) {
        ApiService apiService = new ApiService();
        ConverteDados converteDados = new ConverteDados();

        // Obtém os dados da API
        String json = apiService.querry(nomeLivro);
        Response response = converteDados.converteDados(json, Response.class);

        // Mapeia a resposta para uma lista de VolumeInfo
        List<VolumeInfo> livros = response.items().stream()
                .map(c -> new VolumeInfo(c.info().titulo(),
                        c.info().autores(), c.info().descricao(), c.info().dataDePublicacao(), c.info().categoria(),
                        c.info().avaliacao(), c.info().numeroDePaginas(), c.info().tipo(), c.info().Imgem()))
                .collect(Collectors.toList());
        // Salva livros no banco de dados, se existirem
        if (!livros.isEmpty()) {
            livros.forEach(this::salvarLivro);
        }

        return livros;
    }

    private void salvarLivro(VolumeInfo volumeInfo) {
        Livro livro = new Livro(volumeInfo);
        salvarLivro(livro);
    }

    public void salvarLivro(Livro livro) {
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
    public void salvarCliente(Cliente cliente) {
        try {
            clienteRepository.save(cliente);
        } catch (DataIntegrityViolationException e) {
            // Logar a exceção se necessário
            System.out.println("Tentativa de inserir um livro com dados duplicados ou violação de integridade: " + e.getMessage());
            // Você pode optar por não fazer nada ou lidar com a situação de outra forma
        } catch (Exception e) {
            // Captura outras exceções, se necessário
            System.out.println("Erro ao salvar o livro: " + e.getMessage());
        }
    }
    public void salvarEmprestimo(EmprestimoDTO emprestimoDTO){
        var cliente = emprestimoDTO.clienteId();
        var livro = emprestimoDTO.livroId();
        var data = emprestimoDTO.dataDevolucao();

        Optional<Livro> livroPesquisado = livroRepository.findById(livro);
        Optional<Cliente> clientePesquisado = clienteRepository.findById(cliente);

        if (livroPesquisado.isPresent() && clientePesquisado.isPresent()){
            var clienteEncontrado = clientePesquisado.get();
            Emprestimo emprestimo = new Emprestimo(clienteEncontrado,List.of(livroPesquisado.get()), data);
            emprestimoRepository.save(emprestimo);
        }

    }
    public List<Cliente> buscarCliente() {
        return clienteRepository.findAll();
    }

    public List<Emprestimo> buscarEmprestimos() {
        return emprestimoRepository.findAll();
    }
}
