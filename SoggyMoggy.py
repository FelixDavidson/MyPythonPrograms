print """
Welcome young traveler.
I will be your narrator for the duration of this game.

You find yourself in a tavern surrounded by  warriors and merchants alike
A dark figure approaches you. He is wearing a dark robe with a red rope.
He ask if you can help him. Bein the kind hearted man you are you say yes.
He says, \"A few men from my brotherhood have gone missing on a hike to Mount Mendakai.
They were suppoed to return two weeks ago. When they did not return we asked
a group of brothers to go looking for them. They left a week ago and still have
not returned. I pray you search for them and you will be rewared greatly.\"
Do you accept or refuse?
"""
begin = raw_input("> ")

if begin == "accept":
    print """
He thanks you graciously giving you a map and a staff."
He says, \"May God bless you, I will pray for your return\"
\nYou start on your adventure. As you walk up to a large fork in the road
You see two paths. One is covered in a white sticky substance. The other, is just as
disgusting because it is crawling with mororgs. These creatures are known for rubbing themselves
furiously against people walking by and grunting \"Errrrrro, Errrrrro, Errrrrro\"
Which path do you take?
"""
    path = raw_input("> ")
    if path == "1" or "one" or "One":
        print """You start down the path. Not before long you are struggling to walk through all the
white. Soon your vision begins to fade. Your arms feel heavy. You begin to lose consiousness
Do you give up or pray?"""

        white = raw_input("> ")

        if white == "give up":
            print "This is where it ends for you."

        elif white == "pray":
            print "You clasp your hands in prayer. You pray to a God."
            print "Which one do you pray to?"
            print "Shadowman\nCthulhu\nJesus Christ\nAllah\nGreek Gods\nSatan"

            god = raw_input("> ")

            if god == "Shadowman" or "Shadowman":
                print "You begin to pray to your savior.\nYou hear his voice"
                print """
He says,
\"Your services to the overlords is appreciated. Our complete
assimilation of this dimension... will now... proceed\""""

    elif path == "2" or "two" or "Two":
        print """"""

elif begin == "refuse":
    print "You respond, \"Forgive me brother for I am not up to such a task\""
    print "He says, \"Understandable. Farwell and thank you for listening to my tale.\""
    raw_input("Goodbye?")
