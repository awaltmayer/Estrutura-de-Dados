from modelos.produto import Produto
from modelos.cliente import Cliente
from modelos.venda import Venda

from estruturas.lista_encadeada import ListaEncadeada
from estruturas.fila_vendas import FilaVendas
from estruturas.pilha_operacoes import PilhaOperacoes

from dados.csv_manager import garantir_arquivo, ler_csv, salvar_csv


lista_produtos = ListaEncadeada()
lista_clientes = ListaEncadeada()

fila_vendas = FilaVendas()
pilha_operacoes = PilhaOperacoes()


ARQ_CLIENTES = "dados/clientes.csv"
ARQ_PRODUTOS = "dados/produtos.csv"
ARQ_VENDAS = "dados/vendas.csv"

def carregar_dados():

    garantir_arquivo(ARQ_CLIENTES, ["id_cliente", "nome"])
    garantir_arquivo(ARQ_PRODUTOS, ["id_produto", "nome", "quantidade", "preco"])
    garantir_arquivo(ARQ_VENDAS, ["id_venda", "id_cliente", "id_produto", "quantidade", "valor_total"])

    clientes = ler_csv(ARQ_CLIENTES)

    for linha in clientes:

        cliente = Cliente(int(linha[0]), linha[1])
        lista_clientes.inserir(cliente)

    produtos = ler_csv(ARQ_PRODUTOS)

    for linha in produtos:

        produto = Produto(int(linha[0]), linha[1], int(linha[2]), float(linha[3]))
        lista_produtos.inserir(produto)

    vendas = ler_csv(ARQ_VENDAS)

    for linha in vendas:

        venda = Venda(int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3]), float(linha[4]))
        fila_vendas.enfileirar(venda)

def salvar_dados():

    dados_clientes = []

    atual = lista_clientes.inicio

    while atual:

        cliente = atual.dado

        dados_clientes.append([cliente.id_cliente, cliente.nome])

        atual = atual.proximo

    salvar_csv(ARQ_CLIENTES, ["id_cliente", "nome"], dados_clientes)

    dados_produtos = []

    atual = lista_produtos.inicio

    while atual:

        produto = atual.dado

        dados_produtos.append([produto.id_produto, produto.nome, produto.quantidade, produto.preco])

        atual = atual.proximo

    salvar_csv(ARQ_PRODUTOS, ["id_produto", "nome", "quantidade", "preco"], dados_produtos)

    dados_vendas = []

    for venda in fila_vendas.vendas:

        dados_vendas.append([venda.id_venda, venda.id_cliente, venda.id_produto, venda.quantidade, venda.valor_total])

    salvar_csv(ARQ_VENDAS, ["id_venda", "id_cliente", "id_produto", "quantidade", "valor_total"], dados_vendas)

def mostrar_menu():

    print("\n===== MENU ESTOQUE DE BEBIDAS =====")

    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar bebida")
    print("4 - Listar bebidas")
    print("5 - Pesquisar bebida")
    print("6 - Realizar venda")
    print("7 - Ver fila de vendas")
    print("8 - Desfazer última operação")
    print("9 - Exibir valor total do estoque")
    print("10 - Exibir valor total de vendas")
    print("11 - Exibir clientes e valores gastos")
    print("12 - Sair")

def cadastrar_cliente():

    try:

        id_cliente = int(input("ID do cliente: "))
        nome = input("Nome do cliente: ")

        cliente = Cliente(id_cliente, nome)

        lista_clientes.inserir(cliente)

        pilha_operacoes.empilhar(("cliente", cliente))

        salvar_dados()

        print("Cliente cadastrado")

    except:
        print("Erro ao cadastrar cliente")


def listar_clientes():

    lista_clientes.listar()

def cadastrar_produto():

    try:

        id_produto = int(input("ID da bebida: "))
        nome = input("Nome da bebida: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        produto = Produto(id_produto, nome, quantidade, preco)

        lista_produtos.inserir(produto)

        pilha_operacoes.empilhar(("produto", produto))

        salvar_dados()

        print("Produto cadastrado")

    except:
        print("Erro ao cadastrar produto")


def listar_produtos():

    lista_produtos.listar()


def pesquisar_produto():

    try:

        id_busca = int(input("ID da bebida: "))

        produto = lista_produtos.buscar_por_id(id_busca)

        if produto:
            print(produto)
        else:
            print("Produto não encontrado")

    except:
        print("Erro na pesquisa")

def realizar_venda():

    try:

        id_venda = int(input("ID da venda: "))
        id_cliente = int(input("ID do cliente: "))
        id_produto = int(input("ID do produto: "))
        quantidade = int(input("Quantidade: "))

        cliente = lista_clientes.buscar_por_id(id_cliente)
        produto = lista_produtos.buscar_por_id(id_produto)

        if not cliente or not produto:
            print("Cliente ou produto não encontrado")
            return

        if produto.quantidade < quantidade:
            print("Estoque insuficiente")
            return

        produto.quantidade -= quantidade

        valor_total = quantidade * produto.preco

        venda = Venda(id_venda, id_cliente, id_produto, quantidade, valor_total)

        fila_vendas.enfileirar(venda)

        pilha_operacoes.empilhar(("venda", venda))

        salvar_dados()

        print("Venda realizada")

    except:
        print("Erro na venda")


def ver_fila_vendas():

    fila_vendas.listar()


def desfazer_operacao():

    operacao = pilha_operacoes.desempilhar()

    if not operacao:
        print("Nada para desfazer")
        return

    tipo, objeto = operacao

    if tipo == "venda":

        produto = lista_produtos.buscar_por_id(objeto.id_produto)

        if produto:
            produto.quantidade += objeto.quantidade

        if fila_vendas.vendas:
            fila_vendas.vendas.pop()

        salvar_dados()

        print("Venda desfeita")

def valor_total_estoque():

    atual = lista_produtos.inicio

    total = 0

    while atual:

        produto = atual.dado

        total += produto.quantidade * produto.preco

        atual = atual.proximo

    print("Valor total do estoque: R$", total)


def total_vendas():

    total = 0

    for venda in fila_vendas.vendas:

        total += venda.valor_total

    print("Total de vendas: R$", total)


def clientes_valores_gastos():

    gastos = {}

    for venda in fila_vendas.vendas:

        gastos[venda.id_cliente] = gastos.get(venda.id_cliente, 0) + venda.valor_total

    for id_cliente, total in gastos.items():

        cliente = lista_clientes.buscar_por_id(id_cliente)

        if cliente:
            print(cliente.nome, "gastou R$", total)

def main():

    carregar_dados()

    while True:

        mostrar_menu()

        try:

            opcao = int(input("Escolha: "))

            if opcao == 1:
                cadastrar_cliente()

            elif opcao == 2:
                listar_clientes()

            elif opcao == 3:
                cadastrar_produto()

            elif opcao == 4:
                listar_produtos()

            elif opcao == 5:
                pesquisar_produto()

            elif opcao == 6:
                realizar_venda()

            elif opcao == 7:
                ver_fila_vendas()

            elif opcao == 8:
                desfazer_operacao()

            elif opcao == 9:
                valor_total_estoque()

            elif opcao == 10:
                total_vendas()

            elif opcao == 11:
                clientes_valores_gastos()

            elif opcao == 12:
                break

            else:
                print("Opção inválida")

        except:
            print("Entrada inválida")


if __name__ == "__main__":
    main()

