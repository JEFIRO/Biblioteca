package com.jefiro.Biblioteca.sevice.traducao;

import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record DadosResposta( @JsonAlias(value = "translatedText") String textoTraduzido) {
}