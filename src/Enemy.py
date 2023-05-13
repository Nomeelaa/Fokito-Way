import random

import pygame

import settings

class Enemy:
    def __init__(self, x: int, y: int) -> None:
        self.in_play = True