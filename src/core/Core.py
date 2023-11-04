#!/usr/bin/env python3
import pygame

class Core:

    def init_screen(self) -> None:
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])

    def __init__(self, screen_width=700, screen_height=700) -> None:
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.init_screen()
        self.is_running = True

    def run(self) -> None:
        """ Run the core instance
        """
        
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.screen.fill((200,55,100))
            pygame.display.flip()
        pygame.quit()