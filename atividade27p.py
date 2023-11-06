#pegar a frase.
frase = str(input('Digite um nome')).upper().replace(" ","")
#inverter.
invertido=frase[::-1]
#verificar se a frase é um palindromo
if frase == invertido:
    print("palíndromo")
else:
    print("não é palíndromo")