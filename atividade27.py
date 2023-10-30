# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES. 

frase = str(input('Digite um nome'))
frase = frase.upper().replace(" ","") #tratando ela 
#inverter a palavra e tratar ela 
invertido = frase.upper() [::-1] # inverter a string com [::-1] 
invertido = invertido.replace(" ", "") # removo qulquer espaço que tenha 

if frase == invertido:
    print("palíndromo")
else:
    print("não é palíndromo")