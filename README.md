Manipulação de Arquivos CSV em Python
Este projeto fornece funções simples para criar, ler e salvar arquivos CSV.

Funções
garantir_arquivo(nome_arquivo, cabecalho)
Cria o arquivo com cabeçalho caso não exista.

ler_csv(nome_arquivo)
Lê o CSV ignorando o cabeçalho e retorna uma lista de listas. Retorna lista vazia se o arquivo não existir.

salvar_csv(nome_arquivo, cabecalho, dados)
Sobrescreve o arquivo, escreve o cabeçalho e salva os dados.

Exemplo de uso
arquivo = "dados.csv"
cabecalho = ["Nome", "Idade", "Estado"]

# garante o arquivo
garantir_arquivo(arquivo, cabecalho)

# leitura
dados = ler_csv(arquivo)

# adiciona registro
dados.append(["Pedro", "22", "RS"])

# salva alterações
salvar_csv(arquivo, cabecalho, dados)
Observações
Utiliza encoding UTF-8
Estrutura de dados: lista de listas
Código voltado para uso simples e reutilizável
