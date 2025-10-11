CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    cpf VARCHAR(14) NOT NULL
);

CREATE TABLE Betoneiras (
    id_betoneira INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    statuss BOOLEAN NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

CREATE TABLE Alugueis (
    id_aluguel INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_betoneira INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_betoneira) REFERENCES Betoneiras(id_betoneira)
    )