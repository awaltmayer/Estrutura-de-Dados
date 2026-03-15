from modelos.produto import Produto
from modelos.cliente import Cliente
from modelos.venda import Venda

produto = Produto(1, "Coca-Cola", 50, 6.50)

print("Teste Produto:")
print(produto)
print()

cliente = Cliente(1, "João Silva")

print("Teste Cliente:")
print(cliente)
print()

venda = Venda(1, cliente.id_cliente, produto.id_produto, 3, 19.50)

print("Teste Venda:")
print(venda)

from estruturas.fila_vendas import FilaVendas
from estruturas.pilha_operacoes import PilhaOperacoes
from modelos.venda import Venda

fila = FilaVendas()
pilha = PilhaOperacoes()

venda1 = Venda(1, 1, 1, 2, 13.00)

fila.enfileirar(venda1)
pilha.empilhar("venda realizada")

print("Fila de vendas:")
fila.listar()

print("\nDesfazendo operação:")
print(pilha.desempilhar())

#Gurizada, criei esse arquivo para testar as classes e estruturas que criamos. Vocês podem rodar esse código para verificar se tudo está funcionando corretamente. Se tiverem dúvidas ou encontrarem algum erro, me avisem!