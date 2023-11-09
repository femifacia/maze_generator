#!/usr/bin/env python3

import pygame

class Scene:
    
    def loop(self, args : list) -> None:
        if self.loop_ptr:
            self.loop_ptr(args)
            return
        while self.is_running and self.core.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    self.core.is_running = False
            self.core.screen.fill(self.background_color)
            pygame.display.flip()
        pygame.quit()

    def __init__(self, core, loop_ptr  = None) -> None:
        self.loop_ptr = loop_ptr
        self.button_arr = []
        self.core = core
        self.background_color = (10,55,160)
        self.is_running = True
    
    def add_button(self, button) -> None:
        self.button_arr.append(button)