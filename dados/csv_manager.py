import csv
import os 

def garantir_arquivo(nome_arquivo, cabecalho):
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(cabecalho)

def ler_csv(nome_arquivo):

    dados = []

    if not os.path.exists(nome_arquivo):
        return dados

    try:

        with open(nome_arquivo, "r", newline="", encoding="utf-8") as arquivo:

            leitor = csv.reader(arquivo)

            next(leitor, None)

            for linha in leitor:

                dados.append(linha)

    except Exception as erro:

        print("Erro ao ler arquivo:", erro)

    return dados


def salvar_csv(nome_arquivo, cabecalho, dados):

    try:

        with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow(cabecalho)

            for linha in dados:

                escritor.writerow(linha)

    except Exception as erro:

        print("Erro ao salvar arquivo:", erro)

    #ler e salvar os dados em arquivos csv