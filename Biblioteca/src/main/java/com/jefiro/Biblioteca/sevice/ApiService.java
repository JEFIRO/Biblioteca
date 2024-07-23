package com.jefiro.Biblioteca.sevice;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ApiService {
    public String querry(String pesquisa)  {
        String url = "https://www.googleapis.com/books/v1/volumes?q="
                + pesquisa.replace(" ", "+") + "&filter=partial&key=AIzaSyAKoYdGnOYnLYC7O8xxql3SucrmB5qGHSw";

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url)).build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            return response.body();

        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
