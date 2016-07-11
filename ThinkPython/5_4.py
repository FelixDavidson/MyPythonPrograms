def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print 'No'
    else:
        print 'Yes'

def try_tri():
    print 'You have three sticks. Choose 3 lengths that make a triangle.'

    a = int(raw_input('Choose a length for a:\n'))
    b = int(raw_input('Choose a length for b:\n'))
    c = int(raw_input('Choose a length for c:\n'))

    is_triangle(a, b, c)

try_tri()
