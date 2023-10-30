# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida

velocidade = float(input("digite sua velocidade"))

#se a condição(velocidade>60), entra e exculta o bloco verdadeiro ou falso
if velocidade > 60:
    # verdadeiro
    multa = (velocidade - 60) * 7
    print(f"Sua multa é de R$ {multa}")
else:
    #falso
    print("velocidade permitida!")