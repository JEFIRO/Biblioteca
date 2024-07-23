package com.jefiro.Biblioteca.repository;

import com.jefiro.Biblioteca.modelos.Emprestimo;
import org.springframework.data.jpa.repository.JpaRepository;


public interface EmprestimoRepository extends JpaRepository<Emprestimo, Long> {

}
