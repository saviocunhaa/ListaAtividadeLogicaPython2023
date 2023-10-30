# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso = []
for i in range(5):
    kg = float(input("digite seu peso: "))
    peso.append(kg)

peso2 = sorted(peso)

print(peso2[0], peso2[4])
    