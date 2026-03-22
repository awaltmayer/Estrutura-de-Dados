from typing import Any, Optional, Tuple


class PilhaOperacoes:

    def __init__(self) -> None:
        self.operacoes: list[Tuple[str, Any]] = []

    def empilhar(self, operacao: Tuple[str, Any]) -> None:
        self.operacoes.append(operacao)

    def desempilhar(self) -> Optional[Tuple[str, Any]]:
        if not self.operacoes:
            return None
        return self.operacoes.pop()

    def esta_vazia(self) -> bool:
        return len(self.operacoes) == 0
