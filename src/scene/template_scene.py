#!/usr/bin/env python3

import pygame

import scene
import button
import maze_object
import integer_box

def generate_rectangle_maze_function(info : list) -> None:
    scene = info[0]
    if not 'maze' in scene.graphical_elements_map:
        graph = maze_object.RectangleMaze(50,80,(10,140))
        scene.graphical_elements_map['maze'] = graph
        scene.graphical_elements_arr.append(graph)
    else:
        del scene.graphical_elements_map['maze']
        graph = maze_object.RectangleMaze(50,80,(10,140))
        scene.graphical_elements_map['maze'] = graph
        scene.graphical_elements_arr.append(graph)

def generate_rectangle_maze(core) -> scene.Scene:
    elm = scene.Scene(core, "generate_rectangle_maze")
    generate_button = button.TextButton(text_normal="      GENERATE       ", text_hover="      GENERATE       ", ptr_bound=generate_rectangle_maze_function)
    elm.add_button(generate_button)
    elm.add_graphical_element(integer_box.IntegerBox(), "height")
    elm.add_graphical_element(integer_box.IntegerBox((80,10),legend=" width "), "width")
    return elm

def select_type_maze_generate_scene(core) -> scene.Scene:
    elm = scene.Scene(core,"select_type_maze_generate")
    rectangle_button = button.TextButton(text_normal="      RECTANGLE       ", text_hover="      RECTANGLE       ", scene_name_bound="generate_rectangle_maze")
    elm.add_button(rectangle_button)    
    return elm

def main_scene(core) -> scene.Scene:
    elm = scene.Scene(core,'main')
    generate_button = button.TextButton(text_normal="      GENERATE MAZE       ", text_hover="      GENERATE MAZE       ", scene_name_bound="select_type_maze_generate")
    quit_button = button.TextButton(y=150,text_normal="      QUIT       ", text_hover="      QUIT       ", scene_name_bound="quit")
    elm.add_button(quit_button)
    elm.add_button(generate_button)
    
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