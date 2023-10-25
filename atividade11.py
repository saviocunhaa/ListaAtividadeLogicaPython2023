# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("digite a km"))

if km >= 200:
    valorPassagem = km * 0.50
    print(f"Valor da Passagem é: R$ {valorPassagem}")
else: 
    valorPassagem = km * 0.45
    print(f"Valor da Passagem é: R$ {valorPassagem}")
    