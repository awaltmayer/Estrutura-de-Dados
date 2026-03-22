from dataclasses import dataclass


@dataclass
class Venda:
    id_venda: int
    id_cliente: int
    id_produto: int
    quantidade: int
    valor_total: float

    def __str__(self) -> str:
        return (
            f"Venda {self.id_venda} | Cliente: {self.id_cliente} | "
            f"Produto: {self.id_produto} | Quantidade: {self.quantidade} | "
            f"Total: R$ {self.valor_total:.2f}"
        )