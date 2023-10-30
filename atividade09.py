#Exercício Python 09: faça um software que verifique entre 2 numeros qual o maior

#digitar 2 numeros 
numero01 = int(input("digite o numero 01"))
numero02 = int(input("digite o numero 02"))

#no if(se) faz um processo de comparação e entra na verdadeira ou falsa
if numero01 > numero02:
    print(f"{numero01} maior que {numero02}") #clausula verdadeira
else:
    print(f"{numero02} maior que {numero01}") #clausula falsa
    
