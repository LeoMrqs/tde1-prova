nome_arquivo = input("Digite o nome do arquivo de entrada: ")

with open(nome_arquivo, 'r') as file:
    num_operacoes = int(file.readline().strip())

    for _ in range(num_operacoes):
        operacao = file.readline().strip()
        conjunto1 = set(file.readline().strip().split(", "))
        conjunto2 = set(file.readline().strip().split(", "))

        if operacao == "U":
            resultado = conjunto1.union(conjunto2)
            nome_operacao = "União"
        elif operacao == "I":
            resultado = conjunto1.intersection(conjunto2)
            nome_operacao = "Interseção"
        elif operacao == "D":
            resultado = conjunto1.difference(conjunto2)
            nome_operacao = "Diferença"
        elif operacao == "C":
            resultado = {(x, y) for x in conjunto1 for y in conjunto2}
            nome_operacao = "Produto cartesiano"


        print(f"{nome_operacao}: conjunto 1 {{{', '.join(map(str, conjunto1))}}}, conjunto 2 {{{', '.join(map(str, conjunto2))}}}. Resultado: {{{', '.join(map(str, resultado))}}}")


