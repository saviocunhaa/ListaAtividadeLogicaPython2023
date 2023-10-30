# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso = []
for i in range(5):
    kg = float(input("digite seu peso: "))
    peso.append(kg)

peso2 = sorted(peso) #sorted() pega a lsita e coloca em ordem organizada(crescente) armazeno ele em uma nova variavel chamada peso 2 

#se a lista ja esta organizada eu pego apenas o priemiro indice [0] e o ultimo[4] e exibir eles 
print(peso2[0], peso2[4])
    