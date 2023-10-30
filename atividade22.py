# Exercício Python 22: Faça um programa que mostre na tela os numeros pares entre 1 e 50 (dica estude range e seus paramentros)

#utilizar o for para que consiga pecorrer entre numero 1 - 50 
for numero in range(1,51):
    #comnpara a variavel numero do for se o resto da divisão for 0 ele exibe o numero no print; 
    if numero % 2 == 0: 
        print(numero)

