#!/usr/bin/env python3
import pygame
from scene import Scene
import scene

class Core:
    
    def init_scene(self) -> None:
        self.add_scene(scene.main_scene(self))
        self.add_scene(scene.quit_scene(self))
        self.add_scene(scene.select_type_maze_generate_scene(self))
        self.add_scene(scene.generate_rectangle_maze(self))
        self.add_scene(scene.solve_maze(self))

    def init_screen(self) -> None:
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        
    def add_scene(self, scene_to_add : Scene) -> None:
        """Add a scene to the Core

        Args:
            scene_to_add (Scene): the scene to add
        """
        self.scene_map[scene_to_add.name] = scene_to_add

    def __init__(self, screen_width=700, screen_height=700) -> None:
        """init the Core

        Args:
            screen_width (int, optional): width of the screen. Defaults to 700.
            screen_height (int, optional): height of the screen. Defaults to 700.
        """
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scene_map = {}
        self.init_screen()
        self.sprite_group = pygame.sprite.Group()
        self.is_running = True
        self.main_scene = "main"
        self.init_scene()

    def run(self) -> None:
        """ Run the core instance
        """
        # We launch the loop function of the scene
        self.scene_map[self.main_scene].loop(None)
        pygame.quit()
        return