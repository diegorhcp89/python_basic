nome = 'Diego'
altura = 1.88
peso = 95
imc = peso / (altura * altura)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso}, quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
print(imc)
