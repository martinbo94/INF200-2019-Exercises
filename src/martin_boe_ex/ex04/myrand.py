# -*- coding: utf-8 -*-

__author__ = 'Martin Bø'
__email__ = 'martinb@nmbu.no'


class LCGrand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = (2**31)-1

    def rand(self):


class ListRand:
    def __init__(self, num_list):
        self.num_list = num_list

    def rand(self):
        if len(self.num_list) is not 0:

            number = self.num_list[0]
            del(self.num_list[0])
            return number
        else:
            raise RuntimeError
