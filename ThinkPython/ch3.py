# 3_3
def right_justify(s):
    x = 70 - len(s)
    print x * ' ' + s

right_justify('allen')

# 3_4
def do_twice(f, value):
    f(value)
    f(value)

def print_spam(value):
    print 'spam' * value

def print_twice(string):
    print string * 2

def do_four(func, value):
    func(value)
    func(value)

do_twice(print_spam, 5)
do_four(print_twice, 'foo')

# 3_5
def piped():
    print '|',' ' * 4, '|', ' ' * 4, '|'

def plusminus():
    print '+', '-' * 4, '+', '-' * 4, '+'

def newplusminus():
    print '+', '-' * 4, '+', '-' * 4, '+', '-' * 4, '+'

def newpiped():
    print '|',' ' * 4, '|', ' ' * 4, '|', ' ' * 4, '|'

def grid():
    plusminus()
    piped()
    piped()
    piped()
    piped()
    plusminus()
    piped()
    piped()
    piped()
    piped()
    plusminus()

grid()

def newgrid():
    newplusminus()
    newpiped()
    newpiped()
    newpiped()
    newpiped()
    newplusminus()
    newpiped()
    newpiped()
    newpiped()
    newpiped()
    newplusminus()
    newpiped()
    newpiped()
    newpiped()
    newpiped()
    newplusminus()

newgrid()
