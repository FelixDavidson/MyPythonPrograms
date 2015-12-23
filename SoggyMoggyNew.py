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


    elif begin in {"refuse", "No", "no", "n"}:
        print "You respond, \"Forgive me brother for I am not up to such a task\""
        print "He says, \"Understandable. Farwell and thank you for listening to my tale.\""
        print "Again?"

        again = raw_input("> ")

        if again in {"Yes", "yes", "y"}:
            intro()
        elif again in {"No", "no", "n"}:
            exit(0)
        else:
            exit(0)

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

intro()
