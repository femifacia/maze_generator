import sys

sys.path.append('../')
import maze_generation_algorythm
rectangle_generate = {"dfs_random",maze_generation_algorythm.dfs_random}

from .rectangle_maze import RectangleMaze
from .create_maze_objects import create_maze_objects_from_file