""" 
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Start state.
"""
from typing import Any, Dict, Tuple
import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings

import pygame

from src.Player import Player
from src.Enemy import Enemy


class PlayState(BaseState):
   def enter(self, **params: dict) -> None:
      self.level = params["level"]
      self.player = params["player"]
      # se actualiza los valores para cuando se vuelva del estado VictoryState
      self.player.x = 20
      self.player.y = 20
      self.score = params.get("score", 0)

      #InputHandler

   def update(self, dt: float) -> None:
      self.player.update(dt)

   def render(self, surface: pygame.Surface) -> None:
      surface.fill((0,0,0))

      render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["tiny"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
        )
      
      self.player.render(surface)

      
      #surface.blit(settings.TEXTURES["play_background"], (0, 0))

   def on_input(self, input_id: str, input_data: InputData) -> None:
      if input_id == "move_left":
            if input_data.pressed:
                self.player.vx = -settings.PLAYER_SPEED
                self.player.position = 1
            elif input_data.released and self.player.vx < 0:
                self.player.vx = 0
      elif input_id == "move_right":
            if input_data.pressed:
                self.player.vx = settings.PLAYER_SPEED
                self.player.position = 3
            elif input_data.released and self.player.vx > 0:
                self.player.vx = 0
      
      if input_id == "move_up":
         if input_data.pressed:
            self.player.vy = -settings.PLAYER_SPEED
            self.player.position = 0
         elif input_data.released and self.player.vy < 0:
            self.player.vy = 0
      elif input_id == "move_down":
         if input_data.pressed:
            self.player.vy = settings.PLAYER_SPEED
            self.player.position = 2
         elif input_data.released and self.player.vy > 0:
            self.player.vy = 0