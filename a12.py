def calcular_espaco_mb(espaco_em_bytes):
    return espaco_em_bytes / (1024 * 1024)


with open("usuarios.txt", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

usuarios_espacos = {}

for linha in linhas:
    partes = linha.split()
    if len(partes) == 2:
        usuario, espaco_em_bytes = partes
        espaco_em_bytes = int(espaco_em_bytes)
        if usuario not in usuarios_espacos:
            usuarios_espacos[usuario] = 0
        usuarios_espacos[usuario] += espaco_em_bytes


with open("relatorio.txt", "w") as arquivo_saida:
    arquivo_saida.write("ACME Inc.           Uso do espaço em disco pelos usuários\n")
    arquivo_saida.write("-" * 73 + "\n")
    arquivo_saida.write(
        "Nr.  Usuário        Espaço utilizado     % do uso     Espaço Médio\n\n"
    )

    usuarios_ordenados = sorted(
        usuarios_espacos.items(), key=lambda x: x[1], reverse=True
    )

    total_espaco_bytes = sum(usuarios_espacos.values())
    numero_usuarios = len(usuarios_espacos)

    for i, (usuario, espaco_em_bytes) in enumerate(usuarios_ordenados, start=1):
        espaco_em_mb = calcular_espaco_mb(espaco_em_bytes)
        percentagem_uso = (espaco_em_bytes / total_espaco_bytes) * 100
        espaco_medio_mb = calcular_espaco_mb(total_espaco_bytes / numero_usuarios)

        arquivo_saida.write(
            f"{i:<4} {usuario:<15} {espaco_em_mb:.2f} MB"
            f"    {percentagem_uso:.2f}%"
            f"    {espaco_medio_mb:.2f} MB\n"
        )

    arquivo_saida.write(
        "\nEspaço total ocupado: {:.2f} MB\n".format(
            calcular_espaco_mb(total_espaco_bytes)
        )
    )
    arquivo_saida.write(
        "Espaço médio ocupado: {:.2f} MB\n".format(
            calcular_espaco_mb(total_espaco_bytes / numero_usuarios)
        )
    )

print("Relatório gerado com sucesso em 'relatorio.txt'.")
