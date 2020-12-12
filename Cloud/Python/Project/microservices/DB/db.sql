CREATE DATABASE IF NOT EXISTS `UsersDB`;

USE UsersDB;

DROP TABLE IF EXISTS users;
CREATE TABLE `users`(
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    username VARCHAR(35) NOT NULL,
    pass VARCHAR(20) NOT NULL,
    UNIQUE (`username`),
    PRIMARY KEY (`id`)
);

INSERT INTO users (name, username, pass) VALUES ('Juan Sebastian Reyes', 'sebas.reyes', '1234');
INSERT INTO users (name, username, pass) VALUES ('Pepito', 'pepito', '1234');