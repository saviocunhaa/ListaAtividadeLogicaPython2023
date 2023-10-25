# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

n1 = int(input("digite um numero"))
n2 = int(input("digite um numero"))

if n1>n2:
    print(f"{n1} maior")
elif n2>n1:
    print(f"{n2} maior")
else:
    print(f"{n1}={n2}")

