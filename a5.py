# Crie um programa que leia o conteúdo dos arquivos "texto.txt" e "copia.txt", e escreva o conteúdo combinado em um terceiro arquivo chamado "combinado.txt".


def combinar_arquivos(arquivo1, arquivo2, arquivo_combinado):
    try:
        with open(arquivo1, "r") as arquivo1, open(arquivo2, "r") as arquivo2:
            conteudo1 = arquivo1.read()
            conteudo2 = arquivo2.read()
            conteudo_combinado = conteudo1 + "\n" + conteudo2

            with open(arquivo_combinado, "w") as arquivo_combinado:
                arquivo_combinado.write(conteudo_combinado)

            print(
                f"Conteudo dos arquivos '{arquivo1}' e '{arquivo2}' combinado e escritos em '{arquivo_combinado}' com sucesso."
            )
    except FileExistsError as e:
        print(f"Arquivo nao encontrado: {e}")
    except Exception as e:
        print(f"Erro ao combinar os arquivos: {e}")


caminho_arquivo1 = "texto.txt"
caminho_arquivo2 = "copia.txt"
caminho_arquivo_combinado = "combinado.txt"

combinar_arquivos(caminho_arquivo1, caminho_arquivo2, caminho_arquivo_combinado)
