from dataclasses import dataclass


@dataclass
class Cliente:
    id_cliente: int
    nome: str

    def __str__(self) -> str:
        return f"Cadastro: {self.id_cliente} | Nome: {self.nome}"