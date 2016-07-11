def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print "Holy smokes, Fermat was wrong!"
    print "No, that doesn't work"

def debate_fermat():
    print "Step right up and prove Fermat's Last Theorem wrong"
    print "He says a**n + b**n != c**n\n"

    a = int(raw_input('What is your chosen value for a?\n'))
    b = int(raw_input('What is your chosen value for b?\n'))
    c = int(raw_input('What is your chosen value for c?\n'))
    n = int(raw_input('What is your chosen value for n?\n'))

    check_fermat(a, b, c, n)

debate_fermat()
