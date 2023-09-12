# Crie um programa que copie o conteúdo do arquivo "texto.txt" para um novo arquivo chamado "copia.txt".


def mudar_local_arquivo(origem, destino):
    try:
        with open(origem, "r") as arquivo_origem:
            conteudo = arquivo_origem.read()
            with open(destino, "w") as arquivo_destino:
                arquivo_destino.write(conteudo)
            print(
                f"Conteudo do arquivo '{origem}' copiada para '{destino}' com sucesso."
            )
    except FileNotFoundError:
        print(f"Arquivo '{origem}' não encontrado. ")
    except Exception as e:
        print(f"Erro ao copiar o arquivo: {e}")


caminho_origem = "texto.txt"
caminha_destino = "copia.txt"

mudar_local_arquivo(caminho_origem, caminha_destino)
