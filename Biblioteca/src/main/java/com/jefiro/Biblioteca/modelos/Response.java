package com.jefiro.Biblioteca.modelos;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import java.util.List;
@JsonIgnoreProperties(ignoreUnknown = true)
public record Response(List<Items> items) {
}
