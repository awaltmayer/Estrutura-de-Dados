import csv
import os

def garantir_arquivo(nome_arquivo, cabecalho):
    """Cria o arquivo com cabeçalho apenas se ele não existir."""
    if not os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(cabecalho)
        except IOError as e:
            print(f"Erro ao criar o arquivo {nome_arquivo}: {e}")

def ler_csv(nome_arquivo):
    """Lê os dados do CSV, ignorando o cabeçalho, com tratamento de erros."""
    dados = []
    if not os.path.exists(nome_arquivo):
        return dados

    try:
        with open(nome_arquivo, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)  # Pula o cabeçalho com segurança
            for linha in leitor:
                if linha:  # Ignora linhas vazias acidentais
                    dados.append(linha)
    except IOError as e:
        print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
    
    return dados

def salvar_csv(nome_arquivo, cabecalho, dados):
    """Sobrescreve o arquivo CSV de forma eficiente."""
    try:
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(cabecalho)
            escritor.writerows(dados) 
    except IOError as e:
        print(f"Erro ao salvar o arquivo {nome_arquivo}: {e}")

# --- MELHORIAS IMPLEMENTADAS ---
# Robustez: Adicionado try-except contra erros de permissão ou arquivos abertos.
# Performance: Uso de writerows para gravação em lote (mais rápido).
# Segurança: Proteção contra arquivos vazios e filtragem de linhas em branco.
# Estabilidade: Retorno garantido de lista para evitar erros em cadeia.