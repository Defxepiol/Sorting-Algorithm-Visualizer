import pygame as pg
from settings import *
import random as rd


class SortingAlgorithm:
    def __init__(self, window):
        self.window = window
        self.w_size = 2
        self.max_height = (RES[0]//self.w_size)

        self.lst = [i for i in range(1,self.max_height+1)]
        self.current_sorting_alg = ""
        self.sorting = False

        self.font = pg.font.SysFont(None, 50)
        self.c = 0

    def current_lst(self):
        return self.lst

    def update(self):
        self.draw()
        if self.sorting and self.current_sorting_alg == 'BUBBLESORT':
            try:
                next(self.bubble_sort())
            except StopIteration:
                print(f"{self.current_sorting_alg} done")
                self.current_sorting_alg = ''
                self.sorting = False

        if self.sorting and self.current_sorting_alg == 'INSERTIONSORT':
            try:
                next(self.insertion_sort())
            except StopIteration:
                print(f"{self.current_sorting_alg} done")
                self.current_sorting_alg = ''
                self.sorting = False

        if self.sorting and self.current_sorting_alg == 'SELECTIONSORT':
            try:
                next(self.selection_sort())
            except StopIteration:
                print(f"{self.current_sorting_alg} done")
                self.current_sorting_alg = ''
                self.sorting = False

    def bubble_sort(self):
        for j in range(len(self.lst)-1):
            for i in range(j,len(self.lst)-1):
                if self.lst[i+1] < self.lst[i]:
                    tmp = self.lst[i+1]
                    self.lst[i+1], self.lst[i] = self.lst[i], tmp
                    pg.draw.rect(self.window, 'red',
                                 ((i+1) * self.w_size, 0, self.w_size, self.lst[i] * self.w_size))
                    yield True

        return self.lst

    def insertion_sort(self):
        for i in range(1,len(self.lst)):
            current = self.lst[i]
            d = i-1
            while d >= 0 and self.lst[d] > current:
                self.lst[i], self.lst[d] = self.lst[d], current
                pg.draw.rect(self.window, 'red',
                             ((i) * self.w_size, 0, self.w_size, self.lst[d] * self.w_size))
                d -= 1
                yield True

        return self.lst

    def selection_sort(self):
        for w in range(len(self.lst)):
            _min = self.c
            pg.draw.rect(self.window, 'green',
                         ((_min) * self.w_size, 0, self.w_size, self.lst[_min] * self.w_size))
            for s in range(self.c+1, len(self.lst)):
                if self.lst[_min] > self.lst[s]:
                    _min = s
            self.lst[self.c], self.lst[_min] = self.lst[_min], self.lst[self.c]
            pg.draw.rect(self.window, 'red',
                         ((_min) * self.w_size, 0, self.w_size, self.lst[_min] * self.w_size))
            if self.c == len(self.lst)-1:
                self.c = 0
                return self.lst
            self.c += 1
            yield True



    def draw(self, color='white'):
        t=self.font.render(str(self.current_sorting_alg),1,'black')
        self.window.blit(t,(10,600+20))
        # (100+i,33 + i,145 - i)
        for i in range(len(self.lst)):
             pg.draw.rect(self.window, (10,10,10), (i*self.w_size,0,self.w_size,self.lst[i]*self.w_size))
