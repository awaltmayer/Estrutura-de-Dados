import os

from modelos.produto import Produto
from modelos.cliente import Cliente
from modelos.venda import Venda

from estruturas.lista_encadeada import ListaEncadeada
from estruturas.fila_vendas import FilaVendas
from estruturas.pilha_operacoes import PilhaOperacoes

from dados.csv_manager import garantir_arquivo, ler_csv, salvar_csv

from interface_terminal import *


# =========================
# LIMPAR TELA
# =========================

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# =========================
# ESTRUTURAS
# =========================

lista_produtos = ListaEncadeada()
lista_clientes = ListaEncadeada()

fila_vendas = FilaVendas()
pilha_operacoes = PilhaOperacoes()

ARQ_CLIENTES = "dados/clientes.csv"
ARQ_PRODUTOS = "dados/produtos.csv"
ARQ_VENDAS = "dados/vendas.csv"


# =========================
# CARREGAR DADOS
# =========================

def carregar_dados():

    garantir_arquivo(ARQ_CLIENTES, ["id_cliente", "nome"])
    garantir_arquivo(ARQ_PRODUTOS, ["id_produto", "nome", "quantidade", "preco"])
    garantir_arquivo(ARQ_VENDAS, ["id_venda", "id_cliente", "id_produto", "quantidade", "valor_total"])

    for linha in ler_csv(ARQ_CLIENTES):
        lista_clientes.inserir(Cliente(int(linha[0]), linha[1]))

    for linha in ler_csv(ARQ_PRODUTOS):
        lista_produtos.inserir(Produto(int(linha[0]), linha[1], int(linha[2]), float(linha[3])))

    for linha in ler_csv(ARQ_VENDAS):
        fila_vendas.enfileirar(Venda(int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3]), float(linha[4])))


# =========================
# SALVAR DADOS
# =========================

def salvar_dados():

    dados_clientes = []
    atual = lista_clientes.inicio

    while atual:
        c = atual.dado
        dados_clientes.append([c.id_cliente, c.nome])
        atual = atual.proximo

    salvar_csv(ARQ_CLIENTES, ["id_cliente", "nome"], dados_clientes)

    dados_produtos = []
    atual = lista_produtos.inicio

    while atual:
        p = atual.dado
        dados_produtos.append([p.id_produto, p.nome, p.quantidade, p.preco])
        atual = atual.proximo

    salvar_csv(ARQ_PRODUTOS, ["id_produto", "nome", "quantidade", "preco"], dados_produtos)

    dados_vendas = []
    for v in fila_vendas.vendas:
        dados_vendas.append([v.id_venda, v.id_cliente, v.id_produto, v.quantidade, v.valor_total])

    salvar_csv(ARQ_VENDAS, ["id_venda", "id_cliente", "id_produto", "quantidade", "valor_total"], dados_vendas)


# =========================
# CLIENTES
# =========================

def cadastrar_cliente():
    try:
        id_cliente = int(input("ID cliente: "))
        nome = input("Nome: ")

        if lista_clientes.buscar_por_id(id_cliente):
            erro("ID já existe")
            return

        cliente = Cliente(id_cliente, nome)
        lista_clientes.inserir(cliente)

        pilha_operacoes.empilhar(("cliente", cliente))
        salvar_dados()

        sucesso("Cliente cadastrado")

    except ValueError:
        erro("Entrada inválida")


def listar_clientes():
    mostrar_clientes(lista_clientes)


# =========================
# PRODUTOS
# =========================

def cadastrar_produto():
    try:
        id_produto = int(input("ID bebida: "))
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        if lista_produtos.buscar_por_id(id_produto):
            erro("ID já existe")
            return

        produto = Produto(id_produto, nome, quantidade, preco)
        lista_produtos.inserir(produto)

        pilha_operacoes.empilhar(("produto", produto))
        salvar_dados()

        sucesso("Produto cadastrado")

    except ValueError:
        erro("Entrada inválida")


def listar_produtos():
    mostrar_produtos(lista_produtos)


def pesquisar_produto():
    try:
        id_produto = int(input("ID produto: "))
        produto = lista_produtos.buscar_por_id(id_produto)

        if produto:
            console.print(produto)
        else:
            erro("Produto não encontrado")

    except ValueError:
        erro("Entrada inválida")


# =========================
# VENDAS
# =========================

def realizar_venda():
    try:
        id_venda = int(input("ID venda: "))
        id_cliente = int(input("ID cliente: "))
        id_produto = int(input("ID produto: "))
        quantidade = int(input("Quantidade: "))

        cliente = lista_clientes.buscar_por_id(id_cliente)
        produto = lista_produtos.buscar_por_id(id_produto)

        if not cliente or not produto:
            erro("Cliente ou produto não encontrado")
            return

        if produto.quantidade < quantidade:
            aviso("Estoque insuficiente")
            return

        produto.quantidade -= quantidade

        valor_total = quantidade * produto.preco

        venda = Venda(id_venda, id_cliente, id_produto, quantidade, valor_total)

        fila_vendas.enfileirar(venda)
        pilha_operacoes.empilhar(("venda", venda))

        salvar_dados()

        sucesso("Venda realizada")

    except ValueError:
        erro("Entrada inválida")


def ver_fila_vendas():

    if not fila_vendas.vendas:
        aviso("Nenhuma venda")
        return

    for venda in fila_vendas.vendas:
        console.print(venda)


# =========================
# DESFAZER
# =========================

def desfazer_operacao():

    operacao = pilha_operacoes.desempilhar()

    if not operacao:
        aviso("Nada para desfazer")
        return

    tipo, obj = operacao

    if tipo == "venda":

        produto = lista_produtos.buscar_por_id(obj.id_produto)

        if produto:
            produto.quantidade += obj.quantidade

        if fila_vendas.vendas:
            fila_vendas.vendas.pop()

        sucesso("Venda desfeita")

    salvar_dados()


# =========================
# RELATÓRIOS
# =========================

def valor_total_estoque():

    total = 0
    atual = lista_produtos.inicio

    while atual:
        p = atual.dado
        total += p.quantidade * p.preco
        atual = atual.proximo

    console.print(f"[green]Total estoque: R$ {total:.2f}[/green]")


def total_vendas():

    total = sum(v.valor_total for v in fila_vendas.vendas)

    console.print(f"[green]Total vendas: R$ {total:.2f}[/green]")


def clientes_valores_gastos():

    gastos = {}

    for v in fila_vendas.vendas:
        gastos[v.id_cliente] = gastos.get(v.id_cliente, 0) + v.valor_total

    for id_cliente, total in gastos.items():
        cliente = lista_clientes.buscar_por_id(id_cliente)
        if cliente:
            console.print(f"{cliente.nome} → R$ {total:.2f}")


# =========================
# MAIN
# =========================

def main():

    carregar_dados()

    while True:

        limpar_tela()

        mostrar_titulo()
        mostrar_menu()

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            cadastrar_produto()

        elif opcao == "4":
            listar_produtos()

        elif opcao == "5":
            pesquisar_produto()

        elif opcao == "6":
            realizar_venda()

        elif opcao == "7":
            ver_fila_vendas()

        elif opcao == "8":
            desfazer_operacao()

        elif opcao == "9":
            valor_total_estoque()

        elif opcao == "10":
            total_vendas()

        elif opcao == "11":
            clientes_valores_gastos()

        elif opcao == "12":
            salvar_dados()
            break

        else:
            aviso("Opção inválida")

        pausar()
        limpar_tela()


if __name__ == "__main__":
    main()