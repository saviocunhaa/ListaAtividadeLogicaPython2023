# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
numero = 0
soma = 0
for numero in range(1,501):
    if numero % 3 == 0:
        print(numero)
        soma = soma + numero

print(soma)