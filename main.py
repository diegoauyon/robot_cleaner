import sys
from src.grid import Grid
from src.robot import Robot
from src.cleaner_algorithm import dfs

if __name__ == '__main__':

    debug = False
    # To print all robot movement
    if len(sys.argv) > 1 and sys.argv[1].startswith('debug'):
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
