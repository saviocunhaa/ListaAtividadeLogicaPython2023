# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
numero = []

for i in range(0,6):
    inserirNumero = int(input("DIGITE UM NUMERO "))
    if inserirNumero % 2 == 0:
        numero.append(inserirNumero)


soma = sum(numero)
print(soma)

