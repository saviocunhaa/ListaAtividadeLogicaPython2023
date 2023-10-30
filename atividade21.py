# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time #importar a biblioteca time para uso do intervalo de tempo
for fogos in range(10 ,0 , -1): #utilizar o for para pecorrer e fazer o loop de sequencia de 10 até 0
    print(fogos)
    time.sleep(1)

#fora do for adiciona a ultima interação que será os fogos
print("POW POW 🎆🎆🎆🔥🔥")