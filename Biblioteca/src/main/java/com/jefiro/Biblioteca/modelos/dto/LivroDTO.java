package com.jefiro.Biblioteca.modelos.dto;


import java.util.List;

public record LivroDTO (
        String titulo,
        List<String> autores,
        String dataDePublicacao,
        String imagemUrl
)
{}
