
nome_arquivo_entrada = "a14.txt"
nome_arquivo_saida = "saida3.txt"

with open(nome_arquivo_entrada, "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

conteudo_processado = []


linha_anterior = ""
for linha in linhas:
    
    linha = " ".join(linha.strip().split())
    
    if linha and linha != linha_anterior:
        conteudo_processado.append(linha)
    linha_anterior = linha

with open(nome_arquivo_saida, "w") as arquivo_saida:
    arquivo_saida.write("\n".join(conteudo_processado) + "\n")

print(f"Arquivo processado e salvo com sucesso em '{nome_arquivo_saida}'.")
