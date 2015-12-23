print """
You open your eyes and gasp for air. A wave of blood pours over your body.
You scream in shock, shuffle away, and yell, hoping this place be nothing but a dream.
You try to think what happened.
Nothing...
You get up and look around.\n\n
You are on a beach made of dark sand which glitters with a firey red.
You look up and see a giant bluff. Above it looms a sinister eclipse.
You have a small blade, a rope, a syringe filled with a mysterious liquid,\nand a flask filled with wiskey.\n\n
\" Type help for a list of commands \"
"""

blade = 1
rope = 1
syringe = 1
flask = 1
help = raw_input("> ")

if help == "help":
    print """
    help - list commands
    look - look at your surroundings
    take - grab item
    attack - self explanitory
    drink - self explanitory
    go - travel in a direction
    """
