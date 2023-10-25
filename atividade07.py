# Digite um valor e veja quantos dolares voce poderá comprar: R$

real = float(input("Digite o Valor em Real"))
dolar = float(input("Digite a cotação do dia!"))

conv = real / dolar

print(f"""
    Seu Valor em R$ {real}
    Cotação atual em $ {dolar}

    Valor de Convesão $ {conv}
""")