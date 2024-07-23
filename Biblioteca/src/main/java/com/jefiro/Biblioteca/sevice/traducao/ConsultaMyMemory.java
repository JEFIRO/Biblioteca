package com.jefiro.Biblioteca.sevice.traducao;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.jefiro.Biblioteca.sevice.ApiService;
import com.jefiro.Biblioteca.sevice.ConverteDados;

import java.net.URLEncoder;
public class ConsultaMyMemory {
    public static String obterTraducao(String text) {
        ObjectMapper mapper = new ObjectMapper();

        ApiService consumo = new ApiService();

        String texto = URLEncoder.encode(text);
        String langpair = URLEncoder.encode("en|pt-br");

        String url = "https://api.mymemory.translated.net/get?q=" + texto + "&langpair=" + langpair;

        String json = consumo.querry(url);

        DadosTraducao traducao;
        try {
            traducao = mapper.readValue(json, DadosTraducao.class);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        return traducao.dadosResposta().textoTraduzido();
    }
}