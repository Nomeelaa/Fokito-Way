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


class AttackState(BaseEntityState):
    def enter(self, dir: any) -> None:
        self.player_rect = dir

    def update(self, dt: float) -> None:

###########################################
        if self.entity.into_area:
            if self.entity.handle_tilemap_check_collison():
                self.entity.vy = 0
                self.entity.vx = 0
                self.entity.no_change = True
                self.entity.collision = False
                self.entity.change_state("idle", 0)
                
            else:
                print("collison falsa")
                self_rect = self.entity.get_collision_rect()
                temp_pos = self.where_is(self.player_rect.center, self_rect.center)

                if temp_pos in ("UP", "UP_LEFT", "UP_RIGHT"):
                    if temp_pos == "UP":
                        self.entity.vy = - settings.ENEMY_SPEED
                        self.entity.y += self.entity.vy * dt
                    elif temp_pos == "UP_LEFT":
                        self.entity.vy = -settings.ENEMY_SPEED
                        self.entity.vx = -settings.ENEMY_SPEED
                        self.entity.y += self.entity.vy * dt
                        self.entity.x += self.entity.vx * dt
                    elif temp_pos == "UP_RIGHT":
                        self.entity.vy = -settings.ENEMY_SPEED
                        self.entity.vx = settings.ENEMY_SPEED
                        self.entity.y += self.entity.vy * dt
                        self.entity.x += self.entity.vx * dt

                elif temp_pos in ("DOWN", "DOWN_LEFT", "DOWN_RIGHT"):
                    if temp_pos == "DOWN":
                        self.entity.vy = settings.ENEMY_SPEED
                        self.entity.y += self.entity.vy * dt
                    elif temp_pos == "DOWN_LEFT":
                        self.entity.vy = settings.ENEMY_SPEED
                        self.entity.vx = -settings.ENEMY_SPEED
                        self.entity.y += self.entity.vy * dt
                        self.entity.x += self.entity.vx * dt
                    elif temp_pos == "DOWN_RIGHT":
                        self.entity.vy = settings.ENEMY_SPEED
                        self.entity.vx = settings.ENEMY_SPEED
                        self.entity.y += self.entity.vy * dt
                        self.entity.x += self.entity.vx * dt
                else:
                    self.entity.into_area = False
                    self.entity.change_state("idle", 0)
            #else:
                
        else:
            self.entity.into_area = False
            self.entity.change_state("idle", 0)
###########################################     
        
    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "change" and input_data.pressed:
            self.entity.change_state("idle", 0)
    
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