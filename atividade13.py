# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

n1 = int(input("digite o valor 1"))
n2 = int(input("digite o valor 2"))
n3 = int(input("digite o valor 3"))

if n1 > n2 and n1 > n3:
    print(f"{n1} é maior")
elif n2>n1 and n2>n3:
    print(f"{n2} é maior")
else:
    print(f"{n3} é maior")
    
