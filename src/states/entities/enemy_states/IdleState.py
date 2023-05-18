"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class IdleState for player.
"""
from gale.input_handler import InputData
from random import randint

from src.states.entities.enemy_states.BaseEntityState import BaseEntityState


class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle")
        self.entity.init_direction = randint(0,4)


    def update(self, dt: float) -> None:
        self.entity.change_state("walk", "ss")
        #if self.entity.handle_tilemap_collision_on_bottom():
        #    self.entity.vy = 0
        
