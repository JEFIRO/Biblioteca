package com.jefiro.Biblioteca.modelos.dto;


public record LivroDTODetails(
        String titulo,
        String autores,
        String descricao,
        String dataDePublicacao,
        String categoria,
        Double avaliacao,
        String numeroDePaginas,
        String tipo,
        String imagemUrl) {}
