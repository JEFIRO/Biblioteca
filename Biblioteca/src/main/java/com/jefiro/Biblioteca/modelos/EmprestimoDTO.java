package com.jefiro.Biblioteca.modelos;

public record EmprestimoDTO(
        Long livroId,
        Long clienteId,
        String dataDevolucao) {}
