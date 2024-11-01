import pygame as pg
import random as rd
from constants import *
import numpy as np

class SortingAlgorithms:
    def __init__(self, window):
        self.window = window
        self.values = np.arange(1,window_height//square_size + 1, 1)
        rd.shuffle(self.values)
        self.sorting_generator = None

    def bubble_sort(self):
        n = len(self.values)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.values[j] > self.values[j+1]:
                    # swap if wrong order
                    self.values[j], self.values[j+1] = self.values[j+1], self.values[j]
                    swapped = True
                    yield True        
            if not swapped:
                break      

    def selection_sort(self):
        n = len(self.values)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.values[j] < self.values[min_index]:
                    min_index = j
            if min_index != i:
                self.values[i], self.values[min_index] = self.values[min_index], self.values[i]
                yield True

    def insertion_sort(self):
        n = len(self.values)
        for i in range(1, n):
            key = self.values[i]
            j = i - 1
            while j >= 0 and self.values[j] > key:
                self.values[j + 1] = self.values[j]
                j -= 1
                yield True
            self.values[j + 1] = key
            yield True

    def quick_sort(self, low=0, high=None):
        if high is None:
            high = len(self.values) - 1
        if low < high:
            pivot_index = yield from self.partition(low, high)
            yield from self.quick_sort(low, pivot_index - 1)
            yield from self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = self.values[high]
        i = low - 1
        for j in range(low, high):
            if self.values[j] < pivot:
                i += 1
                self.values[i], self.values[j] = self.values[j], self.values[i]
                yield True
        self.values[i + 1], self.values[high] = self.values[high], self.values[i + 1]
        yield True
        return i + 1