def contar_linhas(arquivo_nome):
    try:
        with open("texto.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            num_linhas = len(linhas)
            return num_linhas
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_nome}' nao foi encontrado.")

        return 0

nome_arquivo = "texto.txt"

numero_linhas = contar_linhas(nome_arquivo)

print(f"O arquivo '{nome_arquivo}' possui {numero_linhas} linhas.")
