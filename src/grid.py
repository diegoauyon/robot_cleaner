#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.direction import Direction
from src.robot import Robot


class GridStatus:
    EMPTY = 0
    NOT_CLEAN = 1
    WALL = 2
    ROBOT = 3


class Grid:
    def __init__(self, grid, debug: False):
        self.__grid = grid
        self.__robot_position = (0, 0)
        self.__cleaned_up_positions = 0
        self.__debug = debug

        grid_x, grid_y = len(grid), len(grid[0])

        for x in range(grid_x):
            for y in range(grid_y):
                grid_status = grid[x][y]
                if grid_status == GridStatus.NOT_CLEAN:
                    self.__cleaned_up_positions += 1
                elif grid_status == GridStatus.ROBOT:
                    grid[x][y] = GridStatus.EMPTY
                    self.__robot_position = (x, y)

    def is_cleared_up(self):
        return self.__cleaned_up_positions == 0

    def move_robot(self, direction):
        m, n = len(self.__grid), len(self.__grid[0])
        x, y = self.__robot_position
        dx, dy = Direction.COORDINATES[direction]
        _x, _y = x + dx, y + dy

        if not (0 <= _x < m and 0 <= _y < n):
            return False

        if self.__grid[_x][_y] == GridStatus.WALL:
            return False

        self.__robot_position = (_x, _y)

        if self.__debug:
            self.print_room()
        return True

    def clean(self, robot):
        if not isinstance(robot, Robot):
            return

        x, y = self.__robot_position

        if self.__grid[x][y] == GridStatus.NOT_CLEAN:
            self.__grid[x][y] = GridStatus.EMPTY
            self.__cleaned_up_positions -= 1

    def print_room(self):
        # for testing
        print(
            '\nRobot position: ', self.__robot_position,
            '\n'.join(str(r) for r in self.__grid),
            '\nNeeds to Clean: ', self.__cleaned_up_positions,
            '\n'
        )
