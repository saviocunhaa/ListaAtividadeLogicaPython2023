# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;

#receber o valor e desconto 
valor = float(input("digite o valor em reais"))
desconto = float(input("Digite a '%' de desconto"))

#desconto 
desconto = (valor * desconto) / 100
resultado = valor-desconto
# exibir resultados
print(f"""
        Valor de Desconto: {desconto}
        Valor Final: {resultado} 
""")