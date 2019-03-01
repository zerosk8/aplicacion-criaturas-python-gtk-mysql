/*
    Script de creación de la base de datos
*/

CREATE DATABASE IF NOT EXISTS Criaturas;
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'contra';
GRANT ALL ON Criaturas.* TO 'usuario'@'localhost' IDENTIFIED BY 'contra';
USE Criaturas;
CREATE TABLE IF NOT EXISTS Criatura(ID INT PRIMARY KEY, Nombre VARCHAR(100), Elemento VARCHAR(10), Ataque INT, Defensa INT, Velocidad INT);
INSERT INTO Criatura VALUES(1,'Zorro salvaje','Fuego',20,25,30);
COMMIT;
