#!/usr/bin/python
# -*- coding: utf-8 -*-

from direction import Direction


class Robot:
    def __init__(self, grid, debug=False):
        self.__grid = grid
        self.__position = Direction.DOWN
        self.__debug=debug

    def _get_position(self):
        return self.__position

    def move(self, direction=None):
        if direction in Direction.COORDINATES:
            self.__position = direction

        return self.__grid.move_robot(self.__position) is True

    def turn_left(self, k=1):
        self.__position = (self.__position + k) % 4

    def turn_right(self, k=1):
        self.__position = (self.__position - k) % 4

    def clean(self):
        self.__grid.clean(self)
