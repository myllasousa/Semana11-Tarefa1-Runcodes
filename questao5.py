salario = float(input(""))
divida = float(input())
mes = 10
ano = 2016
juros = 0.15
aumento = 0.05

while divida <= salario:
    divida += divida * juros
    if mes == 3:
        salario += salario * aumento
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1

print(f'{mes}/{ano}')
