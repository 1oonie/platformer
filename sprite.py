from typing import Any, List

import pygame

class Sprite:
    def __init__(self, rect: pygame.Rect = None, rects: List[pygame.Rect] = None) -> None:
        if rect is not None and rects is not None:
            raise TypeError('rect and rects are mutually exclusive')
        elif rect is None and rects is None:
            raise TypeError('you must provide one of rect or rects')
        
        if rect is not None:
            self._rects: List[pygame.Rect] = [rect]
        elif rects is not None:
            self._rects: List[pygame.Rect] = rects
    
    def is_colliding(self, sprite: 'Sprite') -> bool:
        for rect in self._rects:
            if pygame.Rect.collidelist(rect, sprite._rects):
                return True
        return False
    
    def move(self, /, x: float, y: float) -> None:
        for rect in self._rects:
            rect.move_ip(x, y)
    
    def render(self, display: pygame.surface.Surface, **kwargs: Any) -> None:
        for rect in self._rects:
            pygame.draw.rect(
                surface=display, 
                color=rect.colour, # type: ignore
                rect=rect, 
                **kwargs
            )