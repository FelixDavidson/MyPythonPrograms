import random
min = 1
max = 2

Flip_again = "yes"

while Flip_again == "yes" or Flip_again == "y":
    print "Fliping the coins..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)
    print random.randint(min, max)
    print random.randint(min, max)

    Flip_again = raw_input("Flip the coins again?")
