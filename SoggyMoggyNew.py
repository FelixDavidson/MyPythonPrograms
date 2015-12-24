from sys import exit

def intro():
    print """
Welcome young traveler.
I will be your narrator for the duration of this game.

You find yourself in a tavern surrounded by warriors and merchants alike.
A dark figure approaches you. He is wearing a dark robe with a red rope tied around his waist.

He begins to speak.

He says, \"A few men from my brotherhood have gone missing on a hike to Mount Mendakai.
They were suppoed to return two weeks ago. When they did not return we asked
a group of brothers to go looking for them. They left a week ago and still have
not returned. I pray you, please search for them and you will be rewared greatly.\"
Do you accept or refuse?
"""

    begin = raw_input("> ")

    if begin in {"accept", "y", "yes", "Yes"}:
        paths()

    elif begin in {"refuse", "No", "no", "n"}:
        print "You respond, \"Forgive me brother for I am not up to such a task\""
        print "He says, \"Understandable. Farwell and thank you for listening to my tale.\""
        print "Again?"

        again = raw_input("> ")

        if again in {"Yes", "yes", "y"}:
            intro()
        elif again in {"No", "no", "n"}:
            end("Why did you start playing this anyway?")

    else:
        print "You spelled something wrong try again"
        intro()

def paths():
    print """
He thanks you graciously giving you a map and a staff."
He says, \"May God bless you, I pray for your swift return\"

You start on your adventure. As you walk up to a large fork in the road
You see two paths. One is covered in a white sticky substance. The other, is just as
disgusting because it is crawling with mororgs. These creatures are known for rubbing themselves
furiously against people walking by and grunting \"Errrrrro, Errrrrro, Errrrrro\"
Which path do you take?
"""

def paths():
    print """You start down the path. Not before long you are struggling to walk through all the
white. Soon your vision begins to fade. Your arms feel heavy. You begin to lose consiousness
Do you give up or pray?"""

    white = raw_input("> ")

    if white == "give up":
        end("You stop struggling and let the sluge consume you.")

    elif white == "pray":
        pray()

def pray():
    print "You clasp your hands in prayer. You pray to a God."
    print "Which one do you pray to?"
    print "Shadowman\nCthulhu\nJesus Christ\nAllah\nGreek Gods\nSatan"

    god = raw_input("> ")

    if god in {"Shadowman", "shadowman"}:
        shadowman()
    elif god in {"Cthulhu", "cthulhu"}:
        cthulhu()
    elif god in {"Allah", "allah"}:
        allah()
    elif god in {"Greek", "Greek Gods", "greek Gods", "Greek gods"}:
        greek()
    elif god in {"Satan", "satan"}:
        satan()
    else:
        print "I'm afraid I don't know that god, try again."
        pray()

def shadowman():
    print "shadowman"

def cthulhu():
    print "cthulhu"

def allah():
    print "allah"

def greek():
    print "allah"

def satan():
    print "satan"

def end(reason):
    print reason, "Nice try."
    exit(0)

intro()
