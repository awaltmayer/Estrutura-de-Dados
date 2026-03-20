from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()


def mostrar_titulo():

    console.print(
        Panel.fit(
            "[bold cyan]Sistema de Estoque de Bebidas[/bold cyan]\n"
            "[green]Estrutura de Dados com Python[/green]",
            border_style="cyan"
        )
    )


def mostrar_menu():

    tabela = Table(
        title="Menu Principal",
        box=box.ROUNDED,
        show_lines=True
    )

    tabela.add_column("Opção", justify="center", style="cyan")
    tabela.add_column("Descrição", style="white")

    tabela.add_row("1", "Cadastrar cliente")
    tabela.add_row("2", "Listar clientes")
    tabela.add_row("3", "Cadastrar bebida")
    tabela.add_row("4", "Listar bebidas")
    tabela.add_row("5", "Pesquisar bebida")
    tabela.add_row("6", "Realizar venda")
    tabela.add_row("7", "Ver fila de vendas")
    tabela.add_row("8", "Desfazer última operação")
    tabela.add_row("9", "Valor total do estoque")
    tabela.add_row("10", "Total de vendas")
    tabela.add_row("11", "Clientes e valores gastos")
    tabela.add_row("12", "Sair")

    console.print(tabela)


def mostrar_clientes(lista_clientes):

    tabela = Table(title="Clientes", box=box.ROUNDED)

    tabela.add_column("ID", style="cyan")
    tabela.add_column("Nome", style="white")

    atual = lista_clientes.inicio

    while atual:

        cliente = atual.dado

        tabela.add_row(
            str(cliente.id_cliente),
            cliente.nome
        )

        atual = atual.proximo

    console.print(tabela)


def mostrar_produtos(lista_produtos):

    tabela = Table(title="Bebidas em Estoque", box=box.ROUNDED)

    tabela.add_column("ID", style="cyan")
    tabela.add_column("Bebida")
    tabela.add_column("Quantidade")
    tabela.add_column("Preço")

    atual = lista_produtos.inicio

    while atual:

        produto = atual.dado

        tabela.add_row(
            str(produto.id_produto),
            produto.nome,
            str(produto.quantidade),
            f"R$ {produto.preco:.2f}"
        )

        atual = atual.proximo

    console.print(tabela)


def sucesso(msg):
    console.print(f"[bold green]✔ {msg}[/bold green]")


def erro(msg):
    console.print(f"[bold red]✖ {msg}[/bold red]")


def aviso(msg):
    console.print(f"[bold yellow]⚠ {msg}[/bold yellow]")


def pausar():
    input("\nPressione ENTER para continuar...")