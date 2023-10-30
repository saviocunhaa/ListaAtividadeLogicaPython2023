# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES. 

frase = str(input('Digite um nome'))
frase = frase.upper().replace(" ","") 
invertido = frase.upper() [::-1] 
# .upper() - transforma todos os textos minusculos em maiusculos. 
# [::-1] -> termo para inverter a string
invertido = invertido.replace(" ", "") # .replace() faz com que subistitua o primeiro item pelo segundo, por exemplo nessa linha estou subistituindo qualquer "espaço" por "nada" .replace(" ", "")

#aqui faço o processo de compraração entre as duas Strings 
if frase == invertido:
    print("palíndromo")
else:
    print("não é palíndromo")