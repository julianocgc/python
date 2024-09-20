mult = [[0 for _ in range(3)] for _ in range(10)]

for i in range(10):
    for j in range(3):
        mult[i][j] = (i*j)

print(mult)