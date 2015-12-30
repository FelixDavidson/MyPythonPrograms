x = 6

def example():
    global x # this allows x to be used everywhere

    # If you are not allowed to use global make x a variable in the function
    globx = x

    print x
    print x + 5

    x += 6 # without line 4 variable is not global and will retrun a error
    print x

    return globx # this allows other functions to use this

x = example()

print x
