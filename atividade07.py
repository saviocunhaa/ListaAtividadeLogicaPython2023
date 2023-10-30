# Digite um valor e veja quantos dolares voce poderá comprar: R$

#receber os a valores de real e a cotação do dia em dolar
real = float(input("Digite o Valor em Real"))
dolar = float(input("Digite a cotação do dia!"))

#converter 
conv = real / dolar

#exibir conversão
print(f"""
    Seu Valor em R$ {real}
    Cotação atual em $ {dolar}

    Valor de Convesão $ {conv}
""")