from sys import argv

script, filename = argv

txt = open(filename)

print "Dis da fiel nig? -----> %r" % filename

print txt.read()
print "Dat's da fiel righ?"
