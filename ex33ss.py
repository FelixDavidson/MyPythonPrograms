def happyman(max, step):
    numbers = []
    i = 0

    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

print "The numbers: "

for num in happyman(int(raw_input()), int(raw_input())):
    print num
