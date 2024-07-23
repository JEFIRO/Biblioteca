package com.jefiro.Biblioteca.sevice;

public interface IConvertedados {
    <T> T converteDados(String json, Class<T> classe);
}
