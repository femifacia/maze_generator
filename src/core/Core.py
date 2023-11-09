#!/usr/bin/env python3
import pygame
from scene import Scene
import scene

class Core:
    
    def init_scene(self) -> None:
        self.add_scene("main", scene.main_scene(self))
        self.add_scene("quit", scene.quit_scene(self))

    def init_screen(self) -> None:
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        
    def add_scene(self,name : str ,scene_to_add : Scene) -> None:
        self.scene_map[name] = scene_to_add

    def __init__(self, screen_width=700, screen_height=700) -> None:
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
        self.scene_map[self.main_scene].loop(None)
        pygame.quit()
        return
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.screen.fill((200,55,100))
            pygame.display.flip()
        pygame.quit()