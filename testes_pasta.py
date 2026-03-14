from modelos.produto import Produto
from modelos.cliente import Cliente
from modelos.venda import Venda


# testando produto
produto = Produto(1, "Coca-Cola", 50, 6.50)

print("Teste Produto:")
print(produto)
print()


# testando cliente
cliente = Cliente(1, "João Silva")

print("Teste Cliente:")
print(cliente)
print()


# testando venda
venda = Venda(1, cliente.id_cliente, produto.id_produto, 3, 19.50)

print("Teste Venda:")
print(venda)

#gurizada eu criei esse arquivo aqui pra podermos testar a pasta dos modelos antes, fazemos os proximos assim tmb