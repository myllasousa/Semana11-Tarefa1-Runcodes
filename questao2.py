quantidade = 0
numeros = 0
while True:
    n = int(input(""))
    if n == 0: break
    if n > 0:
        numeros += n
        quantidade += 1
media = numeros / quantidade
print(f'{media:.2f}')
