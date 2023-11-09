#!/usr/bin/env python3
import pygame
from scene import Scene

class Core:
    
    def init_scene(self) -> None:
        self.add_scene("main", Scene(self))

    def init_screen(self) -> None:
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        
    def add_scene(self,name : str ,scene : Scene) -> None:
        self.scene_map[name] = scene

    def __init__(self, screen_width=700, screen_height=700) -> None:
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scene_map = {}
        self.init_screen()
        self.is_running = True
        self.main_scene = "main"
        self.init_scene()

    def run(self) -> None:
        """ Run the core instance
        """
        self.scene_map[self.main_scene].loop(None)
        return
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.screen.fill((200,55,100))
            pygame.display.flip()
        pygame.quit()