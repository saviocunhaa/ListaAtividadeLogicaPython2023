# Escreva um numero e veja qual o seu antecessor e seu sucessor! 
#declaração de numero inteiro (receber pelo input)
numero = int(input("digite um número inteiro"))
#calculo do anterior
ant = numero - 1
#calculo do posterior
prox = numero + 1
#exibir com a concatenação anterior e posterior do numero digitado
print(f"Seu antecessor é {ant} Seu Sucessor é: {prox}") 