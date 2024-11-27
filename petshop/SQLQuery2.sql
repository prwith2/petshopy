create database petshop
use petshop

create table petshop(
	id INT IDENTITY,
	tipo_pet VARCHAR(30),
	nome_pet VARCHAR(30),
	idade INT
)

SELECT * FROM petshop

DROP TABLE petshop