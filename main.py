import pygame as pg
import sys
from sorting_algorithms import SortingAlgorithms
from constants import *
import numpy as np
import random as rd
class Engine:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((window_width, window_height))
        pg.display.set_caption("Sorting Algorithm Visualizer")
        self.clock = pg.time.Clock()

        self.sorting_algorithms = SortingAlgorithms(window = self.window)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                rd.shuffle(self.sorting_algorithms.values)

            if event.type == pg.KEYDOWN and event.key == pg.K_1:
                self.sorting_algorithms.sorting_generator = self.sorting_algorithms.bubble_sort()
            if event.type == pg.KEYDOWN and event.key == pg.K_2:
                self.sorting_algorithms.sorting_generator = self.sorting_algorithms.selection_sort()
            if event.type == pg.KEYDOWN and event.key == pg.K_3:
                self.sorting_algorithms.sorting_generator = self.sorting_algorithms.insertion_sort()
            if event.type == pg.KEYDOWN and event.key == pg.K_4:
                self.sorting_algorithms.sorting_generator = self.sorting_algorithms.quick_sort()

    def update(self):
        self.clock.tick(FPS)
        pg.display.update()

    def draw(self):
        self.window.fill(white)
        # draw array with current values as height position
        for i,value in enumerate(self.sorting_algorithms.values):
            pg.draw.rect(self.window, (255-i*2, 255-i//100, 15+i), (i*square_size, 0, square_size, value*square_size))


    def run(self):
        running = True
        while running:
            self.events()
            if self.sorting_algorithms.sorting_generator:
                try:
                    next(self.sorting_algorithms.sorting_generator)
                except:
                    self.sorting_algorithms.sorting_generator = None
            self.draw()
            self.update()


if __name__ == '__main__':
    engine = Engine()
    engine.run()