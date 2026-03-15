class PilhaOperacoes:

    def __init__(self):
        self.operacoes = []

    def empilhar(self, operacao):
        self.operacoes.append(operacao)

    def desempilhar(self):

        if len(self.operacoes) == 0:
            return None

        return self.operacoes.pop()

    def esta_vazia(self):
        return len(self.operacoes) == 0

#desfaz a ultima operaçao
