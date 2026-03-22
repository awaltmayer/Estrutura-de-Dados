import csv
import os
import tempfile
import logging
from typing import List

logger = logging.getLogger(__name__)


def garantir_arquivo(nome_arquivo: str, cabecalho: List[str]) -> None:
    if not os.path.exists(nome_arquivo):
        try:
            os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
            with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(cabecalho)
        except IOError as e:
            logger.error(f"Erro ao criar o arquivo {nome_arquivo}: {e}")


def ler_csv(nome_arquivo: str) -> List[List[str]]:
    dados: List[List[str]] = []
    if not os.path.exists(nome_arquivo):
        return dados
    try:
        with open(nome_arquivo, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)
            for linha in leitor:
                if linha:
                    dados.append(linha)
    except IOError as e:
        logger.error(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
    return dados


def salvar_csv(nome_arquivo: str, cabecalho: List[str], dados: List[List]) -> None:
    dir_destino = os.path.dirname(nome_arquivo) or "."
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            newline="",
            encoding="utf-8",
            dir=dir_destino,
            delete=False,
            suffix=".tmp"
        ) as tmp:
            escritor = csv.writer(tmp)
            escritor.writerow(cabecalho)
            escritor.writerows(dados)
            tmp_path = tmp.name

        os.replace(tmp_path, nome_arquivo)

    except IOError as e:
        logger.error(f"Erro ao salvar o arquivo {nome_arquivo}: {e}")
        if "tmp_path" in dir() and os.path.exists(tmp_path):
            os.remove(tmp_path)