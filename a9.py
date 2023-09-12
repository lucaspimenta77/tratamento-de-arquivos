
with open("texto.txt", "r") as arquivo:
    
    conteudo = arquivo.read()


quantidade_letras = len([caractere for caractere in conteudo if caractere.isalnum()])

print(f"O arquivo contém {quantidade_letras} letras (excluindo os espaços).")
