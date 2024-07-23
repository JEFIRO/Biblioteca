package com.jefiro.Biblioteca.modelos;

import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import java.awt.*;
import java.time.LocalDate;
import java.util.List;
@JsonIgnoreProperties(ignoreUnknown = true)
public record VolumeInfo(
        @JsonAlias("title") String titulo,
        @JsonAlias("authors") List<String> autores,
        @JsonAlias("description") String descricao,
        @JsonAlias("publishedDate") String dataDePublicacao,
        @JsonAlias("categories") List<String> categoria,
        @JsonAlias("averageRating") Double avaliacao,
        @JsonAlias("pageCount") String numeroDePaginas,
        @JsonAlias("printType") String tipo,
        @JsonAlias("imageLinks") Imagem Imgem){
}
