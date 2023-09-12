#Crie um programa que leia o conteúdo do arquivo "texto.txt" e substitua todas as ocorrências da palavra "mundo" por "Python". O novo conteúdo deve ser escrito em um novo arquivo chamado "modificado.txt".

with open("texto.txt", "r") as arquivo_origem:
    conteudo_original = arquivo_origem.read()


conteudo_modificado = conteudo_original.replace("mundo", "Python")

with open("modificado.txt", "w") as arquivo_modificado:
    arquivo_modificado.write(conteudo_modificado)

print("Substituição concluída e o resultado foi salvo em 'modificado.txt'.")