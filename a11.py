import re


def validar_endereco_ip(ip):
    padrao = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    if re.match(padrao, ip):
        octetos = ip.split(".")

        for octeto in octetos:
            if not (0 <= int(octeto) <= 255):
                return False
        return True
    return False


with open("entrada.txt", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

enderecos_validos = []
enderecos_invalidos = []


for linha in linhas:
    ip = linha.strip()
    if validar_endereco_ip(ip):
        enderecos_validos.append(ip)
    else:
        enderecos_invalidos.append(ip)

with open("saida.txt", "w") as arquivo_saida:
    arquivo_saida.write("[Endereços válidos:]\n")
    for endereco in enderecos_validos:
        arquivo_saida.write(endereco + "\n")
    arquivo_saida.write("\n[Endereços inválidos:]\n")
    for endereco in enderecos_invalidos:
        arquivo_saida.write(endereco + "\n")

print("Relatório gerado com sucesso.")
