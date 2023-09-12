#Crie um programa que leia o conteúdo do arquivo "texto.txt" criado no exercício anterior e o exiba no console.

def ler_arquivo_e_exibir():
    try:
        with open ("texto.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("O arquivo 'texto.txt' não foi encontrado.")

ler_arquivo_e_exibir()