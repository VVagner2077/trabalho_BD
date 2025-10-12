drop table if exists alugueis;
drop table if exists betoneiras;
drop table if exists clientes;

create table clientes(
id_cliente int generated always as identity primary key,
nome varchar(100) not null,
telefone varchar(11) not null,
cpf varchar(14) not null
);

create table betoneiras(
id_betoneira int generated always as identity primary key,
modelo varchar(100) not null,
statuss boolean not null,
valor real not null
);

create table alugueis(
id_aluguel int generated always as  identity primary key,
id_cliente int not null,
id_betoneira int not null,
data_inicio date not null,
data_fim date not null,
foreign key(id_cliente) references clientes(id_cliente),
foreign key(id_betoneira) references betoneiras(id_betoneira)
);