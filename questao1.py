def rendimento(d, j):
    anos = 0
    v_a = d
    while v_a < d * 2:
        v_a += v_a * j / 100
        anos += 1
    return anos

d = float(input(""))
j = float(input(""))

a = rendimento(d, j)
print(a)
