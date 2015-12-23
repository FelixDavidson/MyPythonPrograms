import random
min = 1
max = 2

count = 1
flip = 0

while flip < 48:
    print count
    print random.randint(min, max),
    print random.randint(min, max),
    print random.randint(min, max),
    print random.randint(min, max)

    flip = flip + 1
    count = count + 1
