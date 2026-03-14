class Venda:

    def __init__(self, id_venda, id_cliente, id_produto, quantidade, valor_total):
        self.id_venda = id_venda
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.valor_total = valor_total

    def __str__(self):
        return f"Venda {self.id_venda} | Cliente: {self.id_cliente} | Produto: {self.id_produto} | Quantidade: {self.quantidade} | Total: R$ {self.valor_total:.2f}"
