# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

from datetime import date

data = date.today() # recebo a data do dia automatico 
ano = data.year # retiro apenas o ano da data da linha anterior

dataNascimento = int(input("digite o ano de nascimento")) #receber a data de nascimento

#calcular a idade
idade = ano - dataNascimento


#proceso de compraração
if idade > 18:
    alistamento = idade - 18
    print(f"passou do alistamento {alistamento} anos")
#processo de compraração
elif idade <= 18:
    alistamento = 18 - idade
    print(f"BEM VINDO A GUERRA, ALISTAMENTO MILITAR SERÁ EM: {alistamento} anos")