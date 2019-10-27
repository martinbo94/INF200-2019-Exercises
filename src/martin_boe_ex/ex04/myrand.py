# -*- coding: utf-8 -*-

__author__ = 'Martin Bø'
__email__ = 'martinb@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = (2**31)-1

    def rand(self):
        self.seed = (self.a * self.seed) % self.m
        return self.seed


class ListRand:
    def __init__(self, num_list):
        self.num_list = num_list
        self.index = -1

    def rand(self):
        self.index += 1
        if self.index < len(self.num_list):
            number = self.num_list[self.index]
            return number
        else:
            raise RuntimeError("List is full")


if __name__ == "__main__":
    lcg = LCGRand(52)
    print(lcg.rand())
    list_rand = ListRand([3, 2, 1, 5])
    print(list_rand.rand())
