# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


numero = [] #criar uma lista vazia

# pecorrer atravez do for as 6 posições, sendo que cada loop possa ser armazenado no indice(i) no for
for i in range(0,6):
    inserirNumero = int(input("DIGITE UM NUMERO "))
    # verificação de numero e par
    if inserirNumero % 2 == 0:
        #pego a lista vazia e adiciono atraves da função .append o numeros que são apenas par e que passaram na condição verdadeira 
        numero.append(inserirNumero) 


soma = sum(numero) #função sum() soma todos os item da lista numero de forma automatica
print(soma)

