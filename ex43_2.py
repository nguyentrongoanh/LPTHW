from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and emplement enter().")
        exit(1)

class Engigne(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        print(">>>>>> self.scene_map is an object?", repr(self.scene_map))

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print("///// current_scene", repr(current_scene))
        last_scene = self.scene_map.next_scene('finished')

        print("-----Before the while current_scene is", current_scene)
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            print(">>>> Next scene name is", repr(next_scene_name))
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("-------After the while current_scene is", current_scene)

        current_scene.enter()

class Death(Scene):

    def enter(self):
        print("You are death")
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("You are enter the Central Corridor.")

        action = input("> ")
        if action == "shoot":
            return 'death'

class Finished(Scene):
    def enter(self):
        print("You are fucking alive.")
        return 'finished' # why need return?

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'finished': Finished(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print("Start scene is", repr(self.start_scene))

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        print(">>>>>>> what does opening_scene do", repr(self.next_scene(self.start_scene)))
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engigne(a_map)
a_game.play()
