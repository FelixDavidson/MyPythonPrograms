from sys import exit

x = "> "


def intro():
    print """
Welcome young traveler.
I will be your narrator for the duration of this game.

You find yourself in a tavern surrounded by warriors and merchants alike.
A dark figure approaches you. He is wearing a dark robe with a red rope tied
around his waist.

He begins to speak.

He says, \"A few men from my brotherhood have gone missing on a hike to Mount
Mendakai. They were suppoed to return two weeks ago. When they did not return
we asked a group of brothers to go looking for them. They left a week ago and
still have not returned. I pray you, please search for them and you will be
rewared greatly.\"
Do you accept or refuse?
"""

    begin = raw_input(x)

    if begin in {"accept", "y", "yes", "Yes"}:
        paths()

    elif begin in {"refuse", "No", "no", "n"}:
        print "You say, \"Forgive me brother for I am not up to such a task\""
        print "He responds, \"Understandable. Farwell and thank you for listening to my tale.\""
        print "Again?"

        again = raw_input(x)

        if again in {"Yes", "yes", "y"}:
            intro()
        elif again in {"No", "no", "n"}:
            end("Why did you start playing this anyway?")

    else:
        print "You spelled something wrong. Try again."
        intro()


def paths():
    print """
He thanks you graciously giving you a map and a staff."
He says, \"May God bless you, I pray for your swift return\"

You start on your adventure. As you walk up to a large fork in the road
You see two paths. One is covered in a white sticky substance. The other, is
just as disgusting because it is crawling with mororgs. These creatures are
known for rubbing themselves furiously against people walking by and grunting
\"Errrrrro, Errrrrro, Errrrrro\"
Which path do you take?
"""
    path = raw_input(x)

    if path in {"one", "One", "1"}:
        path1()
    elif path in {"two", "Two", "2"}:
        path2()
    else:
        print "You typed something wrong. Try again."
        paths()


def path1():
    print """You start down the path. Not before long you are struggling to
walk through all the white. Soon your vision begins to fade. Your arms feel
heavy. You begin to lose consiousness.
Do you give up or pray?"""

    white = raw_input(x)

    if white == "give up":
        end("You stop struggling and let the sluge consume you.")

    elif white == "pray":
        pray()


def pray():
    print "You clasp your hands in prayer. You pray to a God."
    print "Which one do you pray to?"
    print "Shadowman\nCthulhu\nJesus Christ\nAllah\nGreek Gods\nSatan"

    god = raw_input(x)

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
    print "You imagine his white facial hair rubbing against your soft cheeks."
    print "You hear his voice, \"Your services to the overlords is appreciated."
    print "Our complete assimilation of this dimension will now proceed\""
    print "You begin to rapidly speed up. All of the molecules in you body warm."
    print "The world begins to turn into a blur. Your see the world age. The civilizations that pass."
    print "You see the beauty. Your schell of emotion begins to shatter."
    print "Something inside you beings to try to tear itself out."
    print "You feel everything. He is no longer needed. You feel the soul that resides in you."
    print "Your mortal body begins to fade. Your scalp begins to crack. The rest of your body follows."
    print "Out of you skin springs a new you."
    print "\"He needs to die,\" a voice in you mind says."
    print "Monster, what do you do?"
    print "Destroy him\nPeace is love"
    Mawg = raw_input(x)

    if Mawg in {"Destroy", "Destroy him", "destroy", "destroy him"}:
        chaos()
    elif Mawg in {"Peace", "peace", "Peace Is Love", "peace Is Love", "peace is Love", "Peace is love", "Peace is Love", "peace is love"}:
        peace()


def chaos():
    print "You decide to spare no one. With your tentacles you smash against the ground."
    print "You elevate into the air. Your body begins to shine."
    print "You scream your name \"MOGGY MOG!\" as you say this, your body becomes one with everything. "
    print "You end it all..."
    print "A blast of anti-matter scatters across the universe making minature black holes everywhere."
    print "Because of the size and density of the hole these wholes begin to consume the universe."
    print "One lands in chest of Shadowman."
    print "The universe fast forwards and he spends millions of years trapped in a frozen state."
    print "In this state his skin, rapidly, yet slowly tears away from his muscle and after his muscle from his bone. His atoms tear at a molecular level."
    print "The universe finally comes to a close as it slowly becomes in itself a black hole taking other universes and expanding."
    print "Soon it beings to tear at the fabric of reality."
    exit("The worlds ends, with you in it, because of your choice.")


def peace():
    pass


def cthulhu():
    print "cthulhu"


def allah():
    print "allah"


def greek():
    print "Greek"


def satan():
    print "satan"


def end(reason):
    print reason, "Nice try."
    exit(0)


def path2():
    print ""
intro()
