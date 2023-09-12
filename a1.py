#Crie um programa que crie um arquivo chamado "texto.txt" e escreva nele o seguinte texto: "Olá, mundo!"

def criar_arquivo_com_texto():
    texto = "Olá, mundo!"

    with open("texto.txt", "w") as arquivo:
        arquivo.write(texto)


criar_arquivo_com_texto()