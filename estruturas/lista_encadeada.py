class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:

    def __init__(self):
        self.inicio = None


    def inserir(self, dado):

        novo_no = No(dado)

        if self.inicio is None:
            self.inicio = novo_no
            return

        atual = self.inicio

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo_no


    def listar(self):

        if self.inicio is None:
            print("Lista vazia")
            return

        atual = self.inicio

        while atual:
            print(atual.dado)
            atual = atual.proximo


    def buscar_por_id(self, id_busca):

        atual = self.inicio

        while atual:

            dado = atual.dado

            if hasattr(dado, "id_produto") and dado.id_produto == id_busca:
                return dado

            if hasattr(dado, "id_cliente") and dado.id_cliente == id_busca:
                return dado

            atual = atual.proximo

        return None


    def remover_por_id(self, id_remover):

        atual = self.inicio
        anterior = None

        while atual:

            dado = atual.dado

            if hasattr(dado, "id_produto") and dado.id_produto == id_remover:
                break

            if hasattr(dado, "id_cliente") and dado.id_cliente == id_remover:
                break

            anterior = atual
            atual = atual.proximo

        if atual is None:
            return False

        if anterior is None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo

        return True

#armazena produtos e clientes usando uma lista encadeada