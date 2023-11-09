#!/usr/bin/env python3

import pygame

import scene
import button

def main_scene(core) -> scene.Scene:
    elm = scene.Scene(core,'main')
    quit_button = button.TextButton(text_normal="      QUIT       ", text_hover="      QUIT       ", scene_name_bound="quit")
    elm.add_button(quit_button)
    
    return elm

def quit_scene(core) -> scene.Scene:
    elm = scene.Scene(core,'quit')
    yes_button = button.TextButton(50,text_normal="      YES       ", text_hover="      YES       ",ptr_bound=quit_function)
    non_button = button.TextButton(150,text_normal="      NO LET's MAZEEEE       ", text_hover="      NO LET's MAZEEEE       ", ptr_bound=back_function)
    elm.add_button(yes_button)
    elm.add_button(non_button)
    
    return elm

def back_function(infos : list) -> None:
    infos[0].is_running = 0

def quit_function(infos : list) -> None:
    infos[0].core.is_running = 0