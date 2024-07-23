package com.jefiro.Biblioteca.repository;

import com.jefiro.Biblioteca.modelos.Cliente;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ClienteRepository extends JpaRepository<Cliente,Long> {

}
