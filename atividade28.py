# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

today = date.today()
anoAtual = today.year


idadeMaior = []
IdadeMenor = []
for i in range(8):
    anoNascimento = int(input("digite seu ano de nascimento"))
    if anoAtual - anoNascimento >= 18:
        idadeMaior.append(anoNascimento)
    else:
        IdadeMenor.append(anoNascimento)
        

print(idadeMaior)
print(IdadeMenor)