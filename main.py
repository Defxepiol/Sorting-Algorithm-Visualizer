import pygame as pg
from settings import *
import sys
from SortingAlgorithm import SortingAlgorithm
import random as rd


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((RES[0],RES[1]+50))
        self.clock = pg.time.Clock()

        pg.display.set_caption("Sorting Algorithm Visualizer")

        self.sorting_alg = SortingAlgorithm(self.window)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                self.sorting_alg.current_sorting_alg = ''
                self.sorting_alg.sorting = False
                rd.shuffle(self.sorting_alg.current_lst())

            if event.type == pg.KEYDOWN and event.key == pg.K_1:
                self.sorting_alg.current_sorting_alg = 'BUBBLESORT'
                self.sorting_alg.sorting = True

            if event.type == pg.KEYDOWN and event.key == pg.K_2:
                self.sorting_alg.current_sorting_alg = 'INSERTIONSORT'
                self.sorting_alg.sorting = True

            if event.type == pg.KEYDOWN and event.key == pg.K_3:
                self.sorting_alg.current_sorting_alg = 'SELECTIONSORT'
                self.sorting_alg.sorting = True

            if event.type == pg.KEYDOWN and event.key == pg.K_4:
                self.sorting_alg.current_sorting_alg = 'SHELLSORT'
                self.sorting_alg.sorting = True

    def update(self):
        pg.display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.window.fill('white')
        self.sorting_alg.update()

    def run(self):
        while True:
            self.events()
            self.draw()
            self.update()


if __name__ == '__main__':
    game = Game()
    game.run()