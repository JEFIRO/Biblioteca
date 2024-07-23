package com.jefiro.Biblioteca.modelos;

import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.jefiro.Biblioteca.modelos.VolumeInfo;

import java.util.List;
@JsonIgnoreProperties(ignoreUnknown = true)
public record Items(@JsonAlias("volumeInfo") VolumeInfo info) {
}
