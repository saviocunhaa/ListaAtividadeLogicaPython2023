# Digite uma metragem e veja isso em cm e mm:
#receber os valores de metros, utilizando float(numeros com virgulas)
metros = float(input("Digite o Valor em Metros \n"))
# transformando cm e mm
cm = metros * 100
mm = metros * 1000

#exibir resultados
print(f"""Convertendo o valor {metros} M
      
      MM = {mm} mm
      CM = {cm} cm 
      
      """)
