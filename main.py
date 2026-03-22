import os
import logging

from modelos.produto import Produto
from modelos.cliente import Cliente
from modelos.venda import Venda

from estruturas.lista_encadeada import ListaEncadeada
from estruturas.fila_vendas import FilaVendas
from estruturas.pilha_operacoes import PilhaOperacoes

from dados.csv_manager import garantir_arquivo, ler_csv, salvar_csv

from interface_terminal import *

logging.basicConfig(
    filename="erros.log",
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")

lista_produtos = ListaEncadeada()
lista_clientes = ListaEncadeada()

fila_vendas = FilaVendas()
pilha_operacoes = PilhaOperacoes()

_BASE = os.path.dirname(os.path.abspath(__file__))
ARQ_CLIENTES = os.path.join(_BASE, "dados", "clientes.csv")
ARQ_PRODUTOS  = os.path.join(_BASE, "dados", "produtos.csv")
ARQ_VENDAS    = os.path.join(_BASE, "dados", "vendas.csv")

def carregar_dados() -> None:

    garantir_arquivo(ARQ_CLIENTES, ["id_cliente", "nome"])
    garantir_arquivo(ARQ_PRODUTOS, ["id_produto", "nome", "quantidade", "preco"])
    garantir_arquivo(ARQ_VENDAS,   ["id_venda", "id_cliente", "id_produto", "quantidade", "valor_total"])

    for i, linha in enumerate(ler_csv(ARQ_CLIENTES), start=2):
        try:
            lista_clientes.inserir(Cliente(int(linha[0]), linha[1]))
        except (ValueError, IndexError) as e:
            logging.error(f"Linha {i} invalida em clientes.csv: {linha} - {e}")
            aviso(f"Linha {i} do arquivo de clientes esta corrompida e foi ignorada.")

    for i, linha in enumerate(ler_csv(ARQ_PRODUTOS), start=2):
        try:
            lista_produtos.inserir(Produto(int(linha[0]), linha[1], int(linha[2]), float(linha[3])))
        except (ValueError, IndexError) as e:
            logging.error(f"Linha {i} invalida em produtos.csv: {linha} - {e}")
            aviso(f"Linha {i} do arquivo de produtos esta corrompida e foi ignorada.")

    for i, linha in enumerate(ler_csv(ARQ_VENDAS), start=2):
        try:
            fila_vendas.enfileirar(
                Venda(int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3]), float(linha[4]))
            )
        except (ValueError, IndexError) as e:
            logging.error(f"Linha {i} invalida em vendas.csv: {linha} - {e}")
            aviso(f"Linha {i} do arquivo de vendas esta corrompida e foi ignorada.")

def salvar_dados() -> None:

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

def cadastrar_cliente() -> None:
    try:
        id_cliente = int(input("ID cliente: "))
        nome = input("Nome: ").strip()

        if not nome:
            erro("Nome nao pode ser vazio")
            return

        if lista_clientes.buscar_por_id(id_cliente, "id_cliente"):
            erro("ID ja existe")
            return

        cliente = Cliente(id_cliente, nome)
        lista_clientes.inserir(cliente)

        pilha_operacoes.empilhar(("cliente", cliente))
        salvar_dados()

        sucesso("Cliente cadastrado")

    except ValueError:
        erro("Entrada invalida - ID deve ser um numero inteiro")


def listar_clientes() -> None:
    mostrar_clientes(lista_clientes)

def cadastrar_produto() -> None:
    try:
        id_produto = int(input("ID bebida: "))
        nome = input("Nome: ").strip()

        if not nome:
            erro("Nome nao pode ser vazio")
            return

        quantidade = int(input("Quantidade: "))
        preco = float(input("Preco: "))

        if quantidade < 0:
            erro("Quantidade nao pode ser negativa")
            return

        if preco <= 0:
            erro("Preco deve ser maior que zero")
            return

        if lista_produtos.buscar_por_id(id_produto, "id_produto"):
            erro("ID ja existe")
            return

        produto = Produto(id_produto, nome, quantidade, preco)
        lista_produtos.inserir(produto)

        pilha_operacoes.empilhar(("produto", produto))
        salvar_dados()

        sucesso("Produto cadastrado")

    except ValueError:
        erro("Entrada invalida - verifique os campos numericos")


def listar_produtos() -> None:
    mostrar_produtos(lista_produtos)


def pesquisar_produto() -> None:
    try:
        id_produto = int(input("ID produto: "))
        produto = lista_produtos.buscar_por_id(id_produto, "id_produto")

        if produto:
            console.print(produto)
        else:
            erro("Produto nao encontrado")

    except ValueError:
        erro("Entrada invalida")

def realizar_venda() -> None:
    try:
        id_venda   = int(input("ID venda: "))
        id_cliente = int(input("ID cliente: "))
        id_produto = int(input("ID produto: "))
        quantidade = int(input("Quantidade: "))

        if quantidade <= 0:
            erro("Quantidade deve ser maior que zero")
            return

        if fila_vendas.buscar_por_id(id_venda):
            erro("ID de venda ja existe")
            return

        cliente = lista_clientes.buscar_por_id(id_cliente, "id_cliente")
        produto  = lista_produtos.buscar_por_id(id_produto, "id_produto")

        if not cliente:
            erro("Cliente nao encontrado")
            return

        if not produto:
            erro("Produto nao encontrado")
            return

        if produto.quantidade < quantidade:
            aviso(f"Estoque insuficiente - disponivel: {produto.quantidade}")
            return

        produto.quantidade -= quantidade
        valor_total = quantidade * produto.preco

        venda = Venda(id_venda, id_cliente, id_produto, quantidade, valor_total)

        fila_vendas.enfileirar(venda)
        pilha_operacoes.empilhar(("venda", venda))

        salvar_dados()

        sucesso(f"Venda realizada - Total: R$ {valor_total:.2f}")

    except ValueError:
        erro("Entrada invalida - verifique os campos numericos")


def ver_fila_vendas() -> None:
    if not fila_vendas.vendas:
        aviso("Nenhuma venda registrada")
        return
    for venda in fila_vendas.vendas:
        console.print(venda)

def desfazer_operacao() -> None:

    operacao = pilha_operacoes.desempilhar()

    if not operacao:
        aviso("Nada para desfazer")
        return

    tipo, obj = operacao

    if tipo == "venda":
        removida = fila_vendas.remover_por_id(obj.id_venda)
        if removida:
            produto = lista_produtos.buscar_por_id(obj.id_produto, "id_produto")
            if produto:
                produto.quantidade += obj.quantidade
            sucesso("Venda desfeita")
        else:
            aviso("Venda nao encontrada na fila - pode ja ter sido processada")

    elif tipo == "cliente":
        if lista_clientes.remover_por_id(obj.id_cliente, "id_cliente"):
            sucesso("Cadastro de cliente desfeito")
        else:
            aviso("Cliente nao encontrado para desfazer")

    elif tipo == "produto":
        if lista_produtos.remover_por_id(obj.id_produto, "id_produto"):
            sucesso("Cadastro de produto desfeito")
        else:
            aviso("Produto nao encontrado para desfazer")

    salvar_dados()

def valor_total_estoque() -> None:
    total = 0.0
    atual = lista_produtos.inicio
    while atual:
        p = atual.dado
        total += p.quantidade * p.preco
        atual = atual.proximo
    console.print(f"[green]Total em estoque: R$ {total:.2f}[/green]")


def total_vendas() -> None:
    total = sum(v.valor_total for v in fila_vendas.vendas)
    console.print(f"[green]Total de vendas: R$ {total:.2f}[/green]")


def clientes_valores_gastos() -> None:
    gastos = {}
    for v in fila_vendas.vendas:
        gastos[v.id_cliente] = gastos.get(v.id_cliente, 0) + v.valor_total

    if not gastos:
        aviso("Nenhuma venda registrada")
        return

    for id_cliente, total in gastos.items():
        cliente = lista_clientes.buscar_por_id(id_cliente, "id_cliente")
        nome = cliente.nome if cliente else f"(cliente {id_cliente} nao encontrado)"
        console.print(f"{nome} -> R$ {total:.2f}")

def main() -> None:

    carregar_dados()

    while True:

        limpar_tela()

        mostrar_titulo()
        mostrar_menu()

        opcao = input("Escolha: ").strip()

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
            sucesso("Dados salvos. Encerrando...")
            break
        else:
            aviso("Opcao invalida - escolha entre 1 e 12")

        pausar()
        limpar_tela()


if __name__ == "__main__":
    main()
