import sys
from grid import Grid
from robot import Robot
from cleaner_algorithm import dfs

if __name__ == '__main__':

    debug = False
    # To print all robot movement
    if sys.argv[1].startswith('debug'):
        debug = True

    grid = Grid([
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 0, 2, 2, 2, 2],
        [0, 1, 0, 3, 0, 1, 0, 1],
    ], debug)
    robot = Robot(grid, debug)

    grid.print_room()

    # -------------------
    dfs(robot)

    # ----------------
    grid.print_room()
