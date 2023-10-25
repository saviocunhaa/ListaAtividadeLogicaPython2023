# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

r1 = int(input("digite valor 1 "))
r2 = int(input("digite valor 2 "))
r3 = int(input("digite valor 3 "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print ("triangulo")
else:
    print ("não é triangulo")