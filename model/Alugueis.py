
from Cliente import Client
from Betoneiras import Betoneira

class Aluguel:
    def __init__(self, id_aluguel,data_inicio,data_devolucao, cliente: Client, betoneira: Betoneira):
        self.id_aluguel = id_aluguel
        self.data_inicio = data_inicio
        self.data_devolucao = data_devolucao
        self.cliente = cliente
        self.betoneira = betoneira
        