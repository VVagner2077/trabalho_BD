class Betoneira:
    def __init__(self, id_betoneira, modelo, status, valor):
        self.id_betoneira = id_betoneira
        self.modelo = modelo
        self.status = status # True para Disponível, False para Alugado
        self.valor = valor   # Preço da diária

    def to_string(self):
        status_str = "Disponível" if self.status else "Alugado"
        return f"ID: {self.id_betoneira}, Modelo: {self.modelo}, Status: {status_str}, Valor da Diária: R${self.valor:.2f}"