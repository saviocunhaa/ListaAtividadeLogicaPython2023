# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
mediaIdade = 0
somaIdade = 0
nomeHomemMaisVelho = ''
maiorIdadeHomem = 0
mulheresMenorQue20 = 0

for i in range(1,5):
    nome = str(input(f"digite o nome da {i}ª pessoa: "))
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("digite M para MASCULINO \n F para FEMININO: \n "))
    sexo = sexo.upper()
    
    somaIdade += idade

    if sexo == "M" and idade >= maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo == "F" and idade < 20:
        mulheresMenorQue20 += 1
    else:
        print("sexo infalido")
   

mediaIdade = somaIdade/4

print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeHomemMaisVelho}.')
print(f'Ao todo são {mulheresMenorQue20} mulheres com menos de 20 anos.')