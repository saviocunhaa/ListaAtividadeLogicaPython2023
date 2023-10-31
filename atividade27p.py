frase = str(input('Digite um nome')).upper().replace(" ","")
invertido=frase[::-1]
if frase == invertido:
    print("palíndromo")
else:
    print("não é palíndromo")