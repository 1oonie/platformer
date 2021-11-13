from pathlib import Path
from typing import List, Optional, Tuple

import pygame

pygame.init()

class _Rect(pygame.Rect):
    def __init__(self, *args, colour: Tuple[int, int, int] = (255, 255, 255), **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.colour = colour

setattr(pygame, 'Rect', _Rect)

from terrain import load_terrain

WIDTH = 500
HEIGHT = 500

display = pygame.display.set_mode((WIDTH, HEIGHT))
print('Created the window.')

terrain = load_terrain(Path('levels') / '1.txt')

clock = pygame.time.Clock()
stopped = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Destroying the window')
            stopped = True
    
    if stopped:
        break
    
    display.fill(color=(0, 0, 0))

    terrain.render(display=display)

    pygame.display.update()
    
pygame.quit()