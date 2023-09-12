
with open("numeros.txt", "r") as arquivo:

    linhas = arquivo.readlines()


soma = 0


for linha in linhas:
    numero = int(linha.strip())  
    soma += numero

print(f"A soma dos números do arquivo é: {soma}")
