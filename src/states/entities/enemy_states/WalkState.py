"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class WalkState for player.
"""
from gale.input_handler import InputData

import random
from random import randint

import settings
from src.states.entities.enemy_states.BaseEntityState import BaseEntityState


class WalkState(BaseEntityState):
    def enter(self, direction: str) -> None:
        init_direction = self.entity.init_direction #= randint(0,3)
        #print(init_direction)
        if init_direction == 0:
            self.entity.change_state("idle")
        if init_direction == 1: #left direction
            self.entity.vx = -settings.ENEMY_SPEED
            self.entity.flipped = True
            self.entity.change_animation("walk")
        elif init_direction == 2:
            self.entity.vx = settings.ENEMY_SPEED
            self.entity.flipped = False
            self.entity.change_animation("walk")
        elif init_direction == 3: #up direction
            self.entity.vy = -settings.ENEMY_SPEED
            self.entity.change_animation("walk_up")
        elif init_direction == 4:
            self.entity.vy = settings.ENEMY_SPEED
            self.entity.change_animation("idle")




        #self.entity.flipped = direction == "left"
        #self.direction = direction
        #

        #if self.entity.flipped:
        #    self.entity.vx *= -1

    def update(self, dt: float) -> None:

        #if not self.entity.check_floor():
        #    self.entity.change_state("fall")

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.ss
        if self.entity.vx != 0:
            self.entity.x += self.entity.vx * dt
        if self.entity.vy != 0:
            self.entity.y += self.entity.vy * dt

        if self.entity.handle_tilemap_collision_on_right():
            self.entity.change_state("idle")
        elif self.entity.handle_tilemap_collision_on_left():
            self.entity.change_state("idle")

        if self.entity.handle_tilemap_collision_on_top():
            self.entity.change_state("idle")
        elif self.entity.handle_tilemap_collision_on_bottom():
            self.entity.change_state("idle")
            


        #if not self.entity.check_floor():
        #    pass
            #self.entity.change_state("fall")
        #print("eeee")
        #print(self.entity.handle_tilemap_collision_all)

        #if self.entity.handle_tilemap_collision_on_bottom():
        #    print("Colision con el piso")

        #self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

        #next_x = self.entity.x + self.entity.vx * dt
        #next_y = self.entity.y + self.entity.vy * dt
        #
        #if self.direction in("left", "right"):
        #    if self.entity.vx < 0:
        #        self.entity.x = max(0, next_x)
        #    else:
        #        self.entity.x = min(self.entity.tilemap.width - self.entity.width, next_x)
        #elif self.direction in ("up", "down"):
        #    if self.entity.vy < 0:
        #        self.entity.y = max(0, next_y)
        #    else:
        #        self.entity.y = min(self.entity.tilemap.height - self.entity.height, next_y)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        pass
        
