CREATE DATABASE IF NOT EXISTS DBdeConan;

GRANT ALL ON DBdeConan.* TO 'conan'@'localhost' IDENTIFIED BY 'crom';

USE DBdeConan;

CREATE TABLE IF NOT EXISTS Criatura(ID INT PRIMARY KEY, Nombre VARCHAR(100), Elemento VARCHAR(10), Ataque INT, Defensa INT, Velocidad INT);

INSERT INTO Criatura VALUES(1, 'Zorro salvaje', 'Fuego', 20, 25, 30);

COMMIT;

