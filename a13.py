
def criar_pagina(conteudo, numero_pagina, nome_arquivo):
    pagina = []
    while conteudo and len(pagina) < 60:
        linha = conteudo.pop(0)
        if len(linha) > 76:
        
            while linha:
                pagina.append(linha[:76])
                linha = linha[76:]
        else:
            pagina.append(linha)
  
    pagina.append(f"Página: {numero_pagina} | Arquivo: {nome_arquivo}")
    return pagina


nome_arquivo_entrada = "a13.txt"
nome_arquivo_saida = "saida2.txt"


with open(nome_arquivo_entrada, "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

paginas = []
conteudo_atual = []
numero_pagina = 1

for linha in linhas:
    conteudo_atual.append(linha.strip())
    if len(conteudo_atual) >= 60:
        paginas.append(criar_pagina(conteudo_atual, numero_pagina, nome_arquivo_entrada))
        numero_pagina += 1
        conteudo_atual = []

if conteudo_atual:
    paginas.append(criar_pagina(conteudo_atual, numero_pagina, nome_arquivo_entrada))


with open(nome_arquivo_saida, "w") as arquivo_saida:
    for pagina in paginas:
        arquivo_saida.write("\n".join(pagina) + "\n\n")

print(f"Arquivo paginado gerado com sucesso em '{nome_arquivo_saida}'.")
