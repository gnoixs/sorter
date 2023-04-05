import pygame
from algorithms.bubble import bubble
from algorithms.counting import counting
from algorithms.heap import heap
from algorithms.insertion import insertion
from algorithms.merge import merge
from algorithms.quick import quick
from algorithms.radix import radix
from algorithms.selection import selection

ALGORITHMS = [
    ['Bubble', bubble, False],
    ['Counting', counting, False],
    ['Heap', heap, False],
    ['Insertion', insertion, False],
    ['Merge*', merge, False],
    ['Quick*', quick, False],
    ['Radix*', radix, False],
    ['Selection', selection, False]
]

WIDTH = 805
HEIGHT = 605
TOP_PAD = 100
SIDE_PAD = 50

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting Visualizer')

#colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (238, 130, 238)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
PASTEL_RED = (255, 153, 153)
PASTEL_YELLOW = (255, 255, 153)
PASTEL_GREEN = (119, 221, 119)
PASTEL_BLUE = (128, 206, 225)
GRADIENT = [
    GREY,
    (160, 160, 160),
    (198, 198, 198)
]