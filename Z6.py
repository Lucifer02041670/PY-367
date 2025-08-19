point = 0

for i in range(2, 51):
    for j in range(2, i):
        if i%j == 0:
            point = 1
    if point != 1:
        print(i)
    point = 0