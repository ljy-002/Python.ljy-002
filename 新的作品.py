a = [1, 5, 2, 30, 4, 7, 3, 6]
di = 0
b = []

for i in range(3,35,5):
    if (a[di] > a[(di + 1)]):
        b.append(a[di])
    else:
        b.append(a[(di + 1)])
    di += 1

print(b)
