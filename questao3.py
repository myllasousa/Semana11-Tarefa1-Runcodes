maior = None
menor = None

while True:
    n = abs(int(input("")))
    if n == 0:
        break
    if n > 0:
        if maior is None or n > maior:
            maior = n
        if menor is None or n < menor:
            menor = n
if maior is not None and menor is not None:
    print(maior)
    print(menor)
else: pass
