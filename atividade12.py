 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("digite o ano"))

if ano % 400 == 0 and ano % 4 == 0 or ano % 100 != 0:
    print("ano bissexto")
else:
    print("não Bissexto")