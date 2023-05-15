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

import settings
from src.Camera import Camera
from src.GameLevel import GameLevel
from src.Player import Player

from gale.text import render_text

from src.Enemy import Enemy


class PlayState(BaseState):
   def enter(self, **enter_params: dict) -> None:
      self.level = enter_params.get("level", 1)
      #create camera
      self.camera = Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
      #create game level
      self.game_level = GameLevel(self.level, self.camera)
      #create tilemap of level
      self.tilemap = self.game_level.tilemap
      #create a player if no pass in params
      self.player = enter_params.get(
            "player", Player(20, 20, self.game_level)
        )
      #set de first animate mode of player
      self.player.change_state("idle")
     
      #self.enemy = enter_params["enemy"]

      #self.enemy.vx = 100
      self.score = enter_params.get("score", 0)

   def update(self, dt: float) -> None:
      self.player.update(dt)

      self.camera.x = max(
         0,
         min(
            self.player.x + 8 - settings.VIRTUAL_WIDTH // 2,
            self.tilemap.width - settings.VIRTUAL_WIDTH,
         )
      )

      self.camera.y = max(
         0,
         min(
            self.player.y + 10 - settings.VIRTUAL_HEIGHT // 2,
            self.tilemap.height - settings.VIRTUAL_HEIGHT,
         ),
      )


      #self.enemy.update(dt)
      #self.enemy.solve_world_boundaries()
      self.game_level.update(dt)

   def render(self, surface: pygame.Surface) -> None:
      surface.fill((0,0,0))

      world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
      self.game_level.render(world_surface)
      

      render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["tiny"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
        )
      
      self.player.render(world_surface)
      #self.enemy.render(surface)
      surface.blit(world_surface, (-self.camera.x, -self.camera.y))

   def on_input(self, input_id: str, input_data: InputData) -> None:
      self.player.on_input(input_id, input_data)
      
