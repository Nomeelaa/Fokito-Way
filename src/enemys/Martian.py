import random
from typing import TypeVar
import pygame
import math

import settings
from src.GameEntity import GameEntity
from src.states.entities import enemy_states

from gale.input_handler import InputData

class Martian(GameEntity):
    def __init__(self, x: int, y: int, game_level: TypeVar("GameLevel")) -> None:
        self.in_play = True
        self.move_direction = random.choice(['left', 'right', 'up', 'down'])
        self.life = 10
        self.scan_area = 150
        self.into_area = False
        super().__init__(
            x,
            y,
            16,
            20,
            "martian",
            game_level,
            states={
                "idle": lambda sm: enemy_states.IdleState(self, sm),
                "walk": lambda sm: enemy_states.WalkState(self, sm),
                "attack": lambda sm: enemy_states.AttackState(self, sm),
            },
           
            animation_defs={
                "idle": {"frames": [0]},
                "idle_horizontal": {"frames": [9]},
                "idle_up": {"frames": [5]},
                "walk": {"frames": [9, 10], "interval": 0.15},
                "walk_up": {"frames": [5, 6], "interval": 0.15},
            },
            type_player=False,
        )

    

    def in_area(self, another: any) -> bool:
        return self.collides_others(self.get_scan_rect(),another)

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
    

    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.state_machine.on_input(input_id, input_data)

    def get_scan_rect(self) -> pygame.Rect:
        return pygame.Rect(
            self.x - (self.scan_area/2),
            self.y - (self.scan_area/2),
            self.width + self.scan_area,
            self.height + self.scan_area
        )
    
    def where_is(self, center_1: tuple[int,int], center_2: tuple[int,int]) -> str:
        if center_1[1] < center_2[1]:
            if center_1[0] < center_2[0]:
                return "UP_LEFT"
            elif center_1[0] > center_2[0]:
                return "UP_RIGHT"
            else:
                return "UP"
        elif center_1[1] == center_2[1]:
            if center_1[0] < center_2[0]:
                return "LEFT"
            elif center_1[0] > center_2[0]:
                return "RIGHT"
        else:
            if center_1[0] < center_2[0]:
                return "DOWN_LEFT"
            elif center_1[0] > center_2[0]:
                return "DOWN_RIGHT"
            else:
                return "DOWN"