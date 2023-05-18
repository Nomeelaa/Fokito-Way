"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class WalkState for player.
"""
from gale.input_handler import InputData

import random
import pygame
from random import randint
from gale.timer import Timer

import settings
from src.states.entities.enemy_states.BaseEntityState import BaseEntityState


class WalkState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.collision = False
        self.entity.init_direction = direction

        #Define Vx or Vy and animation depending of direction
        if direction == "left":
            self.entity.vx = -settings.ENEMY_SPEED
            self.entity.flipped = True
            self.entity.change_animation("walk")
        elif direction =="right":
            self.entity.vx = settings.ENEMY_SPEED
            self.entity.flipped = False
            self.entity.change_animation("walk")
        elif direction == "up":
            self.entity.vy = -settings.ENEMY_SPEED
            self.entity.flipped = True
            self.entity.change_animation("walk_up")
        elif direction =="down":
            self.entity.vy = settings.ENEMY_SPEED
            self.entity.flipped = False
            self.entity.change_animation("idle")
        

        #Set a clock and select a time in case of ocurr a collision
        #Set a random time to change de move
        #And take Time 0 for then calculate _dt
        self.reloj = pygame.time.Clock()
        self.reloj.tick(60)
        self.time_wait = randint(1,3)
        self.time_change_move = randint(5,20)
        self.t0 = pygame.time.get_ticks() / 1000

    def update(self, dt: float) -> None:
        #Calulate Delta Time
        self.t1 = pygame.time.get_ticks() / 1000
        _dt = self.t1 - self.t0

        #In case the entity collide with a world object
        #Change the state to Idle and then again to Walk
        #With new direction. In case that not collide
        #Check if collide with object
        if self.collision:
            if _dt >= self.time_wait:
                self.t0 = self.t1
                self.collision = False
                self.entity.change_state("idle", random.choice(["left", "right", "up", "down"]))
        else:
            if self.entity.handle_tilemap_collision_on_right():
                self.entity.vx = 0
                self.entity.change_animation("idle_horizontal")
                self.collision = True
            elif self.entity.handle_tilemap_collision_on_left():
                self.entity.vx = 0
                self.entity.change_animation("idle_horizontal")
                self.collision = True

            if self.entity.handle_tilemap_collision_on_top():
                self.entity.vy = 0
                self.entity.change_animation("idle_up")
                self.collision = True
            elif self.entity.handle_tilemap_collision_on_bottom():
                self.entity.vy = 0
                self.entity.change_animation("idle")
                self.collision = True        
        
        #If not collide with something and dt > time to change move
        #Set Vx, Vy to 0 and reset the timer to 0...
        if _dt >= self.time_change_move:
            self.t0 = self.t1
            self.entity.vx = 0
            self.entity.vy = 0
            if self.entity.init_direction in ("left", "right"):
                self.entity.change_animation("idle_horizontal")
            elif self.entity.init_direction == "up":
                self.entity.change_animation("idle_up")
            elif self.entity.init_direction == "down":
                self.entity.change_animation("idle")
            self.entity.change_state("idle", "idle")

        
        if self.entity.vx != 0:
            self.entity.x += self.entity.vx * dt
        if self.entity.vy != 0:
            self.entity.y += self.entity.vy * dt


    def on_input(self, input_id: str, input_data: InputData) -> None:
        pass
    
