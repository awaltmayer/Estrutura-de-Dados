from typing import Any, Optional


class No:
    def __init__(self, dado: Any) -> None:
        self.dado = dado
        self.proximo: Optional["No"] = None


class ListaEncadeada:

    def __init__(self) -> None:
        self.inicio: Optional[No] = None

    def inserir(self, dado: Any) -> None:
        novo_no = No(dado)
        if self.inicio is None:
            self.inicio = novo_no
            return
        atual = self.inicio
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def listar(self) -> None:
        if self.inicio is None:
            print("Lista vazia")
            return
        atual = self.inicio
        while atual:
            print(atual.dado)
            atual = atual.proximo

    def buscar_por_id(self, id_busca: int, atributo: str) -> Optional[Any]:
        atual = self.inicio
        while atual:
            dado = atual.dado
            if hasattr(dado, atributo) and getattr(dado, atributo) == id_busca:
                return dado
            atual = atual.proximo
        return None

    def remover_por_id(self, id_remover: int, atributo: str) -> bool:
        atual = self.inicio
        anterior = None
        while atual:
            dado = atual.dado
            if hasattr(dado, atributo) and getattr(dado, atributo) == id_remover:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False