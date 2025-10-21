DROP TABLE IF EXISTS alugueis;
DROP TABLE IF EXISTS betoneiras;
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    CONSTRAINT clientes_cpf_key UNIQUE (cpf),
    CONSTRAINT clientes_telefone_key UNIQUE (telefone)
);

CREATE TABLE betoneiras (
    id SERIAL PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    valor REAL NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('disponivel', 'alugada', 'manutencao'))
);

CREATE TABLE alugueis (
    id SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_betoneira INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_prevista_termino DATE NOT NULL,
    data_termino_real DATE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('ativo', 'finalizado')),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_betoneira) REFERENCES betoneiras(id)
);
