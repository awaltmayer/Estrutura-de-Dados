class Produto:

    def __init__(self, id_produto, nome, quantidade, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"GTIN: {self.id_produto} | Bebida: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f}"