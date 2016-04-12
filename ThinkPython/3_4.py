def do_twice(f, value):
    f(value)
    f(value)

def print_spam(value):
    print 'spam' * value

def print_twice(string):
    print string * 2

do_twice(print_spam, 5)

