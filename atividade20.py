# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM


import random # importando a blioteca random (gera numeros randomicos)

numeroAleatorio = random.randint(0, 5) # cria numeros candomicos de 0 a 5 (0, 5)
numeroUsuario = int(input("digite um valor 0 até 5"))
# comparar os Numeros 
if numeroUsuario <= 5:
    if numeroAleatorio == numeroUsuario:
        print(f"{numeroUsuario} = {numeroAleatorio}")
    else:
        print(f"{numeroUsuario} != {numeroAleatorio}")
else:
    print("valor invalido!")