# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.

status = int(input("""
    digite o status em numeros
    1 - IDOSO
    2 - GESTANTE
    3 - CADEIRANTE
    4 - NENHUMA DAS OPÇÕES
"""))

if status == 1:
    print("IDOSO")
elif status == 2:
    print("GESTANTE")
elif status == 3:
    print("CADEIRANTE")
elif status == 4:
    print("NENHUM DAS OPÇÕES")
else:
    print("valor invalido")



