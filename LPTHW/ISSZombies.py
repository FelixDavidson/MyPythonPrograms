from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "Not really sure what this is for."
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
        print Death.reasons[randint(0, len(self.reasons)-1)]
        print "Wanna try again?"
        again = raw_input("1. Yes\n2. No\n> ")s
        if again in ['yes', '1', 'Yes']:
            a_game.play()
        else:
            exit(1)

class CabinCorridor(Scene):
    '''A corridor that runs past the cabin rooms and
    connects to the EscapePod and BrokenEngRoom.'''
    def enter(self):
        pass

class StorageCorridor(Scene):
    '''A corridor that runs past the StorageRoom,
    RecRoom, EngineRoom'''
    def enter(self):
        pass

class TheBridge(Scene):
    '''Boss in center of room. Connects to Armory,
    StorageCorridor, and CabinCorridor'''
    def enter(self):
        pass

class EscapePod(Scene):
    '''After getting enough parts and fuel it is used to exit.'''
    def enter(self):
        pass

class RecRoom(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        self.scene_name = scene_name

    def opening_scene(self):
        pass



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play
