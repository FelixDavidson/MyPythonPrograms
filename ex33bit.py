def happyman(max, step):
    numbers = []

    for i in range(0, max, step):
        print "At the top i is %d" % i
        numbers.append(i)

    return numbers

print "The numbers: "

for num in happyman(6, 1):
    print num
