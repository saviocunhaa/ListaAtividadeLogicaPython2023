# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#importo a biblioteca datetime
from datetime import date 

today = date.today() #pedo a data atual 
anoAtual = today.year #utilizo apenas o ano


idadeMaior = [] # crio uma lista vazia para adicionar os maiores
IdadeMenor = [] # crio uma lista vazia para adicionar os menores

#criar um loop de 0 até 7 "range(8)" ou seja será repetido esse bloco 7 vezes
for i in range(8):
    anoNascimento = int(input("digite seu ano de nascimento"))
    # faz o processo de comprarção de calculo para saber se e maior de 18 anos 
    if anoAtual - anoNascimento >= 18:

        #.append() adiciona um item na lista caso seja verdadeiro no bloco do if
        idadeMaior.append(anoNascimento)
    else:
        #.append() adiciona um item na lista caso seja falso no bloco do if
        IdadeMenor.append(anoNascimento)
        

print(idadeMaior)
print(IdadeMenor)