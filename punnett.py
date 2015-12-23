def punnett(a, b):
    n = int(len(a)/2)
    x = int(float(len(a)) / n)
    partsA, partsB, gametes = [a[i * x : i * x + x] for i in range(n)], [b[i * x : i * x + x] for i in range(n)], []
    for y in range(1, n):
        g = []
        for index in range(0, n/2 + y):
            for i in partsA[index]:
                for j in partsB[index]:
                    g.append(i+j)
        gametes.append(g)
    return gametes
