# -*- coding: utf-8 -*-

__author__ = 'Martin Bø'
__email__ = 'martinb@nmbu.no'

import random


class Walker:
    def __init__(self, x0, h):
        self.position = x0
        self.home = h
        self.step = 0

    def move(self):
        self.position += random.randint(-1, 1)
        self.step += 1

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.step


def walking(start_position, home, num_times):

    student = Walker(start_position, home)
    steps_list = []

    for i in range(num_times):
        steps = 0
        position = start_position
        while position is not home:
            student.move()
            position = student.get_position()
            steps += 1

        steps_list.append(steps)

    return sorted(steps_list)


if __name__ == "__main__":
    distances = [1, 2, 5, 10, 20, 50, 100]
    for distance in distances:
        s = walking(0, distance, 5)
        print('Distance:  {0}  -> Path lengths: {1}'.format(distance, s))
