
CREATE DATABASE catalogofilmes;
USE catalogofilmes;

CREATE TABLE filmes (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100) NOT NULL,
  diretor VARCHAR(100) NOT NULL,
  genero VARCHAR(50) NOT NULL,
  ano_lancamento INT NOT NULL,
  avaliacao DECIMAL(3,1) NOT NULL
);
