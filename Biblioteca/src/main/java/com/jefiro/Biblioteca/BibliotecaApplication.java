package com.jefiro.Biblioteca;

import com.jefiro.Biblioteca.principal.Principal;
import com.jefiro.Biblioteca.repository.ClienteRepository;
import com.jefiro.Biblioteca.repository.EmprestimoRepository;
import com.jefiro.Biblioteca.repository.LivrosRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BibliotecaApplication  {


    public static void main(String[] args) {
        SpringApplication.run(BibliotecaApplication.class, args);
    }

}
