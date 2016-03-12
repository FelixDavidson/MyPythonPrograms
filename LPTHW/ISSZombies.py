from sys import exit
from random import randint

class Item(object):

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Scene(object):

    def enter(self):
        pass
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        pass

class Death(Scene):
    '''Should have been caused fairly.'''
    def enter(self):
        pass

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

class Armory(Scene):
    '''A room that contains weapons and '''
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

class EngineRoom(Scene):
    '''Contains hypertransporter,'''
    def enter(self):
        pass

class BrokenEngRoom(Scene):

    def enter(self):
        pass

class RecRoom(Scene):

    def enter(self):
        pass

class StorageRoom(Scene):

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
