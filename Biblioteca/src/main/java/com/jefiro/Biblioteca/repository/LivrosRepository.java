package com.jefiro.Biblioteca.repository;

import com.jefiro.Biblioteca.modelos.Cliente;
import com.jefiro.Biblioteca.modelos.Livro;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface LivrosRepository extends JpaRepository<Livro, Long>{

}
