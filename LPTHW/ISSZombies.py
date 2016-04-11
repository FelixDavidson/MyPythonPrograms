from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "Not really sure what this is for"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    '''Should have been caused fairly.'''
    reasons = [
        "It seems something you have done has resulted in your death.",
        "I pray you know that it was your fault you died.",
        "Ok, that was definitely your fault.",
        "NO ONE HAS EVER DONE THAT!"
    ]

    def enter(self):
        print Death.reasons[randint(0, len(self.reasons) - 1)]
        print "Wanna try again?"
        again = raw_input("1. Yes\n2. No")

        if again in ['yes', '1', 'Yes']:
            a_game.play()

        elif again in ['no', '2', 'No']:
            exit(1)

class CabinCorridor(Scene):
    '''A corridor that runs past the cabin rooms and
    connects to the EscapePod and TheBridge.'''
    def enter(self):
        print "You open your eyes. You find yourself in a corridor."
        print "Ahead of you, you see it."
        print "A souless creature. He stares at you with his beady eyes."
        print "He begins to realize your presence and rushes towards you."
        print "He starts on all fours gaining tremendous speed with every"
        print "step."
        print "You can:\nDodge\nRush him\nStand still"

        action = raw_input("> ")

        if action in ['1', 'Dodge', "dodge"]:
            print "You jump to the left as he lurches towards you."
            print "With great force he hits the wall behind you smashing his"
            print "head into a million pieces. You turn back to see his dark"
            print "blood down the glass. You hear screams from other parts of"
            print "the ship. You know more like him are coming. You duck into"
            print "the room closest to you."
            return 'cabin'

        elif action in ['2', 'rush', 'Rush', 'Rush him', 'rush him']:
            print "You drive yourself towards the beast with great speed. To"
            print "your suprise, he does not let up. He runs faster.He  hits"
            print "you with tremendous strength. Your breath leaves your body."
            print "It seems unnatural. He takes you with him as he runs"
            print "towards the window. He smashes you into it. You hear your"
            print "bones shatter against the glass as it begins to crack. "
            print "You think he'd let off after bringing you to death's door,"
            print "but he is unsatisfied. He begins to thrust his head into"
            print "the glass behind it. You have already accepted your fate as"
            print "you hear the glass give and the vacuum of space tear your"
            print "spine from your near death body."
            print "Your sight grows dark."
            return 'death'

        elif action in ['3', 'stand', 'stand still', 'Stand still']:
            print "You stand your ground bracing for impact. As he grows near"
            print "you can tell this was a dumb idea. He hits you like a truck"
            print "killing you almost instantly"
            return 'death'

        else:
            return 'cabcor'


class Cabin(Scene):
    '''A room connecting to the CabinCorridor'''
    def enter(self):
        print "You begin to look around and see two pairs of bunk beds"


class StorageCorridor(Scene):
    '''A corridor that runs past the StorageRoom and
    EngineRoom'''
    def enter(self):
        pass


class TheBridge(Scene):
    '''Boss in center of room. Connects to StorageCorridor
    and CabinCorridor'''
    def enter(self):
        pass


class EscapePod(Scene):
    '''After getting enough parts and fuel it is used to exit.'''
    def enter(self):
        pass


class EngineRoom(Scene):
    '''A room with an engine'''
    def enter(self):
        pass


class Map(object):

    scenes = {}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play
