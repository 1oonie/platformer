from typing import List, Optional
from pathlib import Path

import pygame

from sprite import Sprite

def load_terrain(file: Path) -> Sprite:
    with file.open() as f:
        data = f.read()
    
    out: List[pygame.Rect] = []
    for nrow, row in enumerate(data.split('\n')):
        for nchar, char in enumerate(row):
            if char == '+':
                out.append(pygame.Rect((nrow*20, nchar*20), (20, 20)))
            
    return Sprite(rects=out)