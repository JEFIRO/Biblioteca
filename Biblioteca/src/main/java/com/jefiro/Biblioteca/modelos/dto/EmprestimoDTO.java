package com.jefiro.Biblioteca.modelos.dto;

public record EmprestimoDTO(
        Long livroId,
        Long clienteId,
        String dataDevolucao) {}
