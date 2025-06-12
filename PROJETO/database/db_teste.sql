create database db_teste;
use db_teste;

create table tb_pessoas(
id int not null auto_increment,
nome_pessoas varchar(50) not null,
idade_pessoas int not null,
emial_pessoas varchar (50) not null,
primary key(id)
);

insert into tb_pessoas values
(null, 'Antonio','35', 'antonio@gmail.com'),
(null,'Karla',25,'karla@gmail.com'),
(null, 'Roberto', '19','roberto@gmail.com'),
(null, 'Sara', '23','sara@gmail.com'),
(null, 'Ana','47','ana@gmail.com');

select * from tb_pessoas;
