"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Paddle.
"""
import pygame

import settings

class Player:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64

        # By default, rigth view position
        self.position = 3

        self.texture = settings.TEXTURES["player_sprites_sheets"]
        self.frames = settings.FRAMES["player_positions"]

        self.vx = 0

    def get_collision_rect(self) -> None:
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self, dt: float) -> None:
        next_x = self.x + self.vx * dt

        if self.vx < 0:
            self.x = max(0, next_x)
        else:
            self.x = min(settings.VIRTUAL_WIDTH - self.width, next_x)

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, (self.x, self.y), self.frames[self.position][0])