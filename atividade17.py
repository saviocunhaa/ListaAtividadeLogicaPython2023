# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

from datetime import date

data = date.today()
ano = data.year

dataNascimento = int(input("digite o ano de nascimento"))

idade = ano - dataNascimento

if idade > 18:
    alistamento = idade - 18
    print(f"passou do alistamento {alistamento} anos")
elif idade <= 18:
    alistamento = 18 - idade
    print(f"BEM VINDO A GUERRA, ALISTAMENTO MILITAR SERÁ EM: {alistamento} anos")