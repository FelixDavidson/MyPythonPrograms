apples = 0
oranges = 0
while oranges != -1:
    print "Enter number of apples: "
    apples = int(raw_input())
    print "Enter number of oranges: "
    oranges = int(raw_input())
    if oranges or apples == 0:
        continue
    print apples + oranges
