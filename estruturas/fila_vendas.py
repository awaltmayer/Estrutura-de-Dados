from collections import deque
from typing import Optional
from modelos.venda import Venda


class FilaVendas:

    def __init__(self) -> None:
        self.vendas: deque[Venda] = deque()

    def enfileirar(self, venda: Venda) -> None:
        self.vendas.append(venda)

    def desenfileirar(self) -> Optional[Venda]:
        if not self.vendas:
            return None
        return self.vendas.popleft()

    def remover_por_id(self, id_venda: int) -> bool:
        for i, v in enumerate(self.vendas):
            if v.id_venda == id_venda:
                del self.vendas[i]
                return True
        return False

    def buscar_por_id(self, id_venda: int) -> Optional[Venda]:
        for v in self.vendas:
            if v.id_venda == id_venda:
                return v
        return None

    def listar(self) -> None:
        if not self.vendas:
            print("Nenhuma venda registrada")
            return
        for venda in self.vendas:
            print(venda)
