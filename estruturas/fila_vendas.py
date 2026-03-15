class FilaVendas:

    def __init__(self):
        self.vendas = []

    def enfileirar(self, venda):
        self.vendas.append(venda)

    def desenfileirar(self):

        if len(self.vendas) == 0:
            return None

        return self.vendas.pop(0)

    def listar(self):

        if len(self.vendas) == 0:
            print("Nenhuma venda registrada")
            return

        for venda in self.vendas:
            print(venda)

#registro das vendas em uma fila para manter a ordem de atendimento