class Cliente:
    def __init__(self, id_cliente, nome, telefone, cpf):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def to_string(self):
        return f"ID: {self.id_cliente}, Nome: {self.nome}, Telefone: {self.telefone}, CPF: {self.cpf}"