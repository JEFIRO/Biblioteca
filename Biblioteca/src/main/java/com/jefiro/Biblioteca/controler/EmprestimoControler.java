package com.jefiro.Biblioteca.controler;

import com.jefiro.Biblioteca.modelos.Cliente;
import com.jefiro.Biblioteca.modelos.Emprestimo;
import com.jefiro.Biblioteca.modelos.dto.EmprestimoDTO;
import com.jefiro.Biblioteca.modelos.Livro;
import com.jefiro.Biblioteca.modelos.dto.LivroDTO;
import com.jefiro.Biblioteca.modelos.dto.LivroDTODetails;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api")
public class EmprestimoControler {

    @Autowired
    EmprestimoService service;

    @GetMapping("/livros")
    public List<Livro> livros() {
        return service.buscarLivros();
    }

    @GetMapping("/clientes")
    public List<Cliente> clientes() {
        return service.buscarCliente();
    }


    @GetMapping("/livros/{id}")
    public List<LivroDTODetails> livrosDetails(@PathVariable Long id) {
        List<LivroDTODetails> livro = service.buscarLivrosById(id).stream().map(l -> {
            return new LivroDTODetails(l.getTitulo(), l.getAutores(), l.getDescricao(),
                    l.getDataDePublicacao(), l.getCategoria(), l.getAvaliacao(),
                    l.getNumeroDePaginas(), l.getTipo(), l.getImagemUrl());
        }).collect(Collectors.toList());
        return livro;
    }

    @GetMapping("/livros/buscar")
    public List<LivroDTO> buscarLivros(@RequestParam String nome) {
        List<LivroDTO> livro = service.buscarLivros(nome).stream().map(l -> {
            return new LivroDTO(l.titulo(), l.autores(), formatter(l.dataDePublicacao()), l.Imgem().imagem());
        }).collect(Collectors.toList());
        return livro;
    }
    @GetMapping("/emprestimos")
    public List<Emprestimo> emprestimo() {
        return service.buscarEmprestimos();
    }
    @PostMapping("/clientes/save")
    public ResponseEntity<Cliente> save(@RequestBody Cliente cliente){
        service.salvarCliente(cliente);
        return null;
    }

    @PostMapping("/emprestimos")
    public ResponseEntity<EmprestimoDTO> save(@RequestBody EmprestimoDTO emprestimo){
        service.salvarEmprestimo(emprestimo);
        return null;
    }

    private String formatter(String data) {
        try {
            DateTimeFormatter inputFormatter = DateTimeFormatter.ofPattern("yyyy/MM/dd");

            DateTimeFormatter outputFormatter = DateTimeFormatter.ofPattern("yyyy");

            var date = LocalDate.parse(data.replace("-", "/"), inputFormatter);

            return date.format(outputFormatter);
        } catch (Exception e) {
        }
        try {
            DateTimeFormatter inputFormatter = DateTimeFormatter.ofPattern("yyyy");

            DateTimeFormatter outputFormatter = DateTimeFormatter.ofPattern("yyyy");

            var date = LocalDate.parse(data.replace("-", "/"), inputFormatter);

            return date.format(outputFormatter);
        } catch (Exception e) {
        }
        return "0000";
    }

}

