# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

#inicia variaveis zerada
soma = 0
#iniciar o for que vai de 1 a 500
for i in range(1,501):
    #compara se o numero armazenado na variavel i(indice do for) o resto da divisão for 0 ele exibe e armazena navariavel soma o valor da soma + o ultimo indice
    if i % 3 == 0:
        print(i)
        soma += i

print(f"A soma é: {soma}") #exibe a soma