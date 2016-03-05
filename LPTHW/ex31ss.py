print "Welcom to Soggy Moggy"
print "You enter a dark room with two doors. Do you go through door #1 or door #2 or be a rebel #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giantc bear here eating a cheese cake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your leggs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothingspins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of Jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You stumble around and fall on a knife. Good job!"
    print "But what's this?"
    print "You stand up clinging to life."
    print "You see a poato.\n Do you:"
    print "1. Eat the potato"
    print "2. Shove the potato in you wound"
    print "3. Hail Moggy-Mog?"

    potato = raw_input("> ")

    if potato == "1":
        print "You're a dumbass. You died alone"
    elif potato == "2":
        print "The potato slips inside you. Now you are a potato cyborb."
    else:
        print "He hears your call. He choses you. You teleport to Morg City"
        print "You spread you cheaks and prepare youself for his love"
        print "He enters you."
        print "1. Moan with pleasure"
        print "2. Slap him"
        print "3. Husband him"

        soggymoggy = raw_input("> ")

        if soggymoggy == "1":
            print "He accepts your gift. You spend the rest of your life like this"
        elif soggymoggy == "2":
            print "He growns with pleasure. This envigorates him sending him into a horny rage."
            print "He fills you with his juce to the brim causing you to black out."
#            if #Finish this if
        elif soggymoggy == "3":
            print "He accepts. Everyday you spend your life repeating this process"
        else:
            print "You die of pleasure"
