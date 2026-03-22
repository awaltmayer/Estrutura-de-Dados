Trabalho realizado na matéria de Organização e Abstração na Programação. 

Sistema de Estoque de Bebidas
Projeto desenvolvido para a disciplina de Estrutura de Dados com Python, aplicando conceitos de Programação Orientada a Objetos (POO) e estruturas de dados clássicas em um sistema de gerenciamento de estoque de bebidas via terminal.

Funcionalidades

Cadastro e listagem de clientes e produtos
Realização e acompanhamento de vendas
Desfazer a última operação (clientes, produtos ou vendas)
Relatórios de estoque, total de vendas e gastos por cliente
Persistência dos dados em arquivos CSV


Estruturas de Dados Utilizadas
EstruturaAplicaçãoLista EncadeadaArmazenamento de clientes e produtosFila (deque)Registro de vendas em ordem de chegadaPilhaHistórico de operações para desfazer

Como Executar
Pré-requisitos: Python 3.10+ e a biblioteca rich.
pip install rich
python main.py

Estrutura do Projeto
├── main.py                  # Ponto de entrada e lógica principal
├── interface_terminal.py    # Exibição com Rich (menus, tabelas, mensagens)
├── modelos/
│   ├── cliente.py           # Modelo de Cliente
│   ├── produto.py           # Modelo de Produto
│   └── venda.py             # Modelo de Venda
├── estruturas/
│   ├── lista_encadeada.py   # Lista encadeada
│   ├── fila_vendas.py       # Fila de vendas
│   └── pilha_operacoes.py   # Pilha para desfazer operações
├── dados/
    ├── csv_manager.py       # Leitura e escrita de CSVs
    ├── clientes.csv
    ├── produtos.csv
    └── vendas.csv

Integrantes do grupo:
Augusto Wolfart Altmayer - RA 1138100 
github (awaltmayer)

Gabriel Nunes - RA 1137876
github (gabnunes09)

Geraldo Konig Scheurer - RA 1126596
github (geraldokonig)

Pedro Henrique Fernandes Polita - RA 1138911
github (pedrofpolita-25)

Professor 
Augusto Ortolan 
github (augusto16ortolan)
