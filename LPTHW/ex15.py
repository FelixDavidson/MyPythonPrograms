#takes cmds from the shell, and imports them into argv
from sys import argv
#tells the interpreter argv is the script and filename
script, filename = argv
#opens the file with filename
txt = open(filename)
#prints text with the filename
print "Here's your file %r:" % filename
#reads the text of txt
print txt.read()
#Prints string.
print "Type the filename again:"
#prompts the user with > and takes raw_input
file_again = raw_input("> ")
#opens file_again
txt_again = open(file_again)
#prints the contents of txt_again which is equal to the raw_input entered before
#reads (or outputs txt_again in shell)
print txt_again.read()
