import pygame as pg
from settings import *
import random as rd


class SortingAlgorithm:
    def __init__(self, window):
        self.window = window
        self.w_size = 10
        self.max_height = (RES[0]//self.w_size)

        self.lst = [i for i in range(1,self.max_height+1)]
        self.current_sorting_alg = ""
        self.sorting = False

        self.font = pg.font.SysFont(None, 50)
        self.min_index = 0

        self.bubble = self.bubble_sort()
        self.inser = self.insertion_sort()
        self.select = self.selection_sort()

    def current_lst(self):
        return self.lst

    def update(self):
        self.draw()
        if self.current_sorting_alg == 'BUBBLESORT':
            try:
                next(self.bubble)
            except StopIteration:
                print(f"{self.current_sorting_alg} done")
                self.current_sorting_alg = ''
                self.sorting = False
                self.bubble = self.bubble_sort()
        if self.current_sorting_alg == 'INSERTIONSORT':
            try:
                next(self.inser)
            except StopIteration:
                print(f"{self.current_sorting_alg} done")
                self.current_sorting_alg = ''
                self.sorting = False
                self.inser = self.insertion_sort()

        if self.current_sorting_alg == 'SELECTIONSORT':
            try:
                next(self.select)
            except StopIteration:
                print(f"{self.current_sorting_alg} done")
                self.current_sorting_alg = ''
                self.sorting = False
                self.select = self.selection_sort()
        
    def bubble_sort(self):
        self.sorting = True
        for i in range(len(self.lst)-1):
            for j in range(i+1,len(self.lst)):
                if self.lst[j] < self.lst[i]:
                    tmp = self.lst[i]
                    self.lst[i] = self.lst[j]
                    self.lst[j] = tmp
                    pg.draw.rect(self.window, 'red',((j) * self.w_size, 0, self.w_size, self.lst[j] * self.w_size))
                    yield 
        self.sorting = False
        return self.lst

    def insertion_sort(self):
        self.sorting = True
        for i in range(1,len(self.lst)):
            current = self.lst[i]
            d = i-1
            while d >= 0 and self.lst[d] > current:
                pg.draw.rect(self.window, 'red',((d) * self.w_size, 0, self.w_size, self.lst[d] * self.w_size))
                self.lst[d+1] = self.lst[d]
                d -= 1
                yield
            self.lst[d+1] = current
        self.sorting = False
        return self.lst

    def selection_sort(self):
        self.sorting = True
        for i in range(len(self.lst)):
            min_index = i
            pg.draw.rect(self.window, 'green',((min_index) * self.w_size, 0, self.w_size, self.lst[min_index] * self.w_size))
            for j in range(i+1,len(self.lst)):
                if self.lst[min_index] > self.lst[j]:
                    min_index = j
            pg.draw.rect(self.window, 'red',((min_index) * self.w_size, 0, self.w_size, self.lst[min_index] * self.w_size))
            aux = self.lst[i]
            self.lst[i] = self.lst[min_index]
            self.lst[min_index] = aux
            yield 
        
        self.sorting = False
        return self.lst

    def draw(self, color='white'):
        t=self.font.render(str(self.current_sorting_alg),1,'black')
        self.window.blit(t,(10,600+20))
        # (100+i,33 + i,145 - i)
        for i in range(len(self.lst)):
             pg.draw.rect(self.window, (10,10,10), (i*self.w_size,0,self.w_size,self.lst[i]*self.w_size))
