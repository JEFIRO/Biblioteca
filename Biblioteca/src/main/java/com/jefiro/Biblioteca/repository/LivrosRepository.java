package com.jefiro.Biblioteca.repository;

import com.jefiro.Biblioteca.modelos.Livro;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface LivrosRepository extends JpaRepository<Livro, Long>{
    List<Livro> findTop5ByOrderByDataDePublicacaoDesc();

    List<Livro> findTop5ByOrderByAvaliacaoDesc();
}
