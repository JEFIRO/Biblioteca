package com.jefiro.Biblioteca.modelos;

import java.util.List;

public record LivroDTO (
        String titulo,
        List<String> autores,
        String dataDePublicacao,
        String imagemUrl
)
{}
