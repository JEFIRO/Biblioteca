package com.jefiro.Biblioteca.modelos;


import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record Imagem(
        @JsonAlias("thumbnail") String imagem
) {}
