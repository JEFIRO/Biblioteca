package com.jefiro.Biblioteca.modelos;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Entity
@Table(name = "livro")
public class Livro {
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    Long id;
    @Column(unique = true)
    private String titulo;
    private String autores;
    @Column(length = 10000)
    private String descricao;
    private String dataDePublicacao;
    private String categoria;
    private Double avaliacao;
    private String numeroDePaginas;
    private String tipo;
    private String imagemUrl;

    public Livro() {
    }

    public Livro(VolumeInfo volume) {
        this.titulo = volume.titulo();
        try{this.autores = volume.autores().get(0);} catch (NullPointerException e ){this.autores = null;}
        this.descricao = volume.descricao();
        try {
            DateTimeFormatter inputFormatter = DateTimeFormatter.ofPattern("yyyy/MM/dd");
            DateTimeFormatter outputFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

            var date = LocalDate.parse(volume.dataDePublicacao().replace("-","/"), inputFormatter);

            this.dataDePublicacao = date.format(outputFormatter);

        } catch (Exception e){
            this.dataDePublicacao = volume.dataDePublicacao();
        }
        try{
            this.categoria = volume.categoria().get(0);
        }  catch (NullPointerException e ){

        this.autores = null;
    }
        if (volume.avaliacao() == null) { this.avaliacao = 0.0;}else {this.avaliacao = volume.avaliacao();}
        this.numeroDePaginas = volume.numeroDePaginas();
        this.tipo = volume.tipo();
        this.imagemUrl = volume.Imgem().imagem();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDescricao() {
        return descricao;
    }

    public String getImagemUrl() {
        return imagemUrl;
    }

    public void setImagemUrl(String imagemUrl) {
        this.imagemUrl = imagemUrl;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public String getDataDePublicacao() {
        return dataDePublicacao;
    }

    public void setDataDePublicacao(String dataDePublicacao) {
        this.dataDePublicacao = dataDePublicacao;
    }

    public String getAutores() {
        return autores;
    }

    public void setAutores(String autores) {
        this.autores = autores;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public Double getAvaliacao() {
        return avaliacao;
    }

    public void setAvaliacao(Double avaliacao) {
        this.avaliacao = avaliacao;
    }

    public String getNumeroDePaginas() {
        return numeroDePaginas;
    }

    public void setNumeroDePaginas(String numeroDePaginas) {
        this.numeroDePaginas = numeroDePaginas;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }


    @Override
    public String toString() {
        return "Livro{" +
                "id=" + id +
                ", titulo='" + titulo + '\'' +
                ", autores='" + autores + '\'' +
                ", descricao='" + descricao + '\'' +
                ", dataDePublicacao='" + dataDePublicacao + '\'' +
                ", categoria='" + categoria + '\'' +
                ", avaliacao=" + avaliacao +
                ", numeroDePaginas='" + numeroDePaginas + '\'' +
                ", tipo='" + tipo + '\'' +
                ", imagemUrl='" + imagemUrl + '\'' +
                '}';
    }
}
