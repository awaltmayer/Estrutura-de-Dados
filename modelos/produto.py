from dataclasses import dataclass


@dataclass
class Produto:
    id_produto: int
    nome: str
    quantidade: int
    preco: float

    def __str__(self) -> str:
        return f"GTIN: {self.id_produto} | Bebida: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f}"
