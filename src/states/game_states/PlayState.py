""" 
VGP 2023
Group: DJ-TKD
Project: Fokito Way

Author: Gerardo Montes, Alberto 
gm5072@gmail.com

This file contains the class to define the Start state.
"""
from typing import Any, Dict, Tuple
from random import randint

import pygame

import settings
from src.Camera import Camera
from src.GameLevel import GameLevel

#import Gale Modules
from gale.text import render_text
from gale.timer import Timer
from gale.input_handler import InputData
from gale.state import BaseState

#import Entites class
from src.Player import Player
from src.Enemy import Enemy
from src.enemys.Martian import Martian


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
            "player", Player(18, 18, self.game_level)
        )
      #set de first animate mode of player
      self.player.change_state("idle")

      self.score = enter_params.get("score", 0)
      #create a list of enemy
      self.all_enemy = []
      self.type_enemy = ["martian", "skeleton"]

      if self.level < 2:
         for _ in range(randint(5,10)):
            self.all_enemy.append(Martian(randint(180,486), randint(360,558), self.game_level))
      elif self.level < 10 and self.level > 1 :
         for _ in range(randint(10,30)):
            self.all_enemy.append(Enemy(randint(738,918), randint(3,342), self.game_level))

      for _, enemy in enumerate(self.all_enemy):
         enemy.change_state("idle", "None")
    

      def create_new_enemy():
         for _ in range(randint(1,5)):
            self.all_enemy.append(Enemy(randint(738,918), randint(3,342), self.game_level))
         for _, enemy in enumerate(self.all_enemy):
            enemy.change_state("idle", randint(1,10)) #reset all enemy time

      #Timer.every(60, create_new_enemy, 2)

      self.time_in_play = "00:00"
      #self.time_in_play = "00:00:00"
      self.timer = 0
      self.seconds = 0
      self.minutes = 0
      self.hours = 0

      def count_timer() -> None:
         self.seconds += 1
         if self.seconds == 60 :
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
               self.minutes = 0
               self.hours += 1
         #self.time_in_play = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
         self.time_in_play = f"{self.minutes:02}:{self.seconds:02}"

      Timer.every(1, count_timer)

      #Timer.every(1, countdown_timer) #ejecuta la funcion cada x segundos


   def update(self, dt: float) -> None:
      print("Enemigos: ", len(self.all_enemy))
      if len(self.all_enemy) > 0:

         if self.score % 20 == 0 and self.player.life <= 90:
            self.player.life += 1
            print("recover: ", self.player.life)

         self.player.update(dt, self.seconds)

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
   #############################################################
         for _, enemy in enumerate(self.all_enemy):
            if enemy.in_area(self.player):
               enemy.into_area = True
               enemy.change_state("attack", self.player.get_collision_rect())
            enemy.update(dt, 0)
            
   #############################################################      

         self.game_level.update(dt)

         #Check collision of enemy with player to rest life
         if (self.player.life > 0):
            for _, enemy in enumerate(self.all_enemy):

               if enemy.collides(self.player):
                  print("score: ", self.score)
                  if (self.player.weapon is None):
                     self.player.life -= 1
                  else:
                     enemy.life -= self.player.attack
                     self.player.life -= 1
                  if enemy.life == 0:
                     self.score += 5
                     self.all_enemy.remove(enemy)
                     break
               if self.player.collides(enemy):
                  print("Colision")
            if len(self.all_enemy) == 0:
               self.player.victory = True
         else:
            self.state_machine.change("game_over", score=self.score)
      else:
         if self.player.victory:
            self.state_machine.change("victory", level=self.level, score=self.score)
    

   def render(self, surface: pygame.Surface) -> None:
      surface.fill((0,0,0))

      world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
      self.game_level.render(world_surface)
      

      
      #world_surface.fill((255,255,255), self.player.get_collision_rect())
      self.player.render(world_surface)
      #self.enemy.render(world_surface)

      for _, enemy in enumerate(self.all_enemy):
         #world_surface.fill((255,255,255), enemy.get_scan_rect())
         enemy.render(world_surface)

      surface.blit(world_surface, (-self.camera.x, -self.camera.y))

      #Render Life and BarLife
      render_text(
         surface,
         "Life",
         settings.FONTS["score_tiny"],
         495,
         6,
         (255, 255, 255),
         shadowed=True,
      )

      surface.fill((255,255,255), pygame.Rect(530,4,104,14)) #Rect(x,y,width,height)
      surface.fill((0,0,0), pygame.Rect(532,6,100,10)) #Rect(x,y,width,height)
      surface.fill((255,0,0), pygame.Rect(532,6,self.player.life,10)) #Rect(x,y,width,height)
      
      #Render Score of player
      render_text(
         surface,
         f"Score: {self.score:05}",
         settings.FONTS["score_tiny"],
         settings.VIRTUAL_WIDTH - 90,
         20,
         (255, 255, 255),
         shadowed=True,
      )

      #Render Total Enemy
      if len(self.all_enemy) > 0:
         render_text(
            surface,
            f"For Dead: {len(self.all_enemy):03}",
            settings.FONTS["score_tiny"],
            settings.VIRTUAL_WIDTH - 100,
            35,
            (255, 255, 255),
            shadowed=True,
         )
      else:
         render_text(
            surface,
            f"For Dead: {0:03}",
            settings.FONTS["score_tiny"],
            settings.VIRTUAL_WIDTH - 100,
            35,
            (255, 255, 255),
            shadowed=True,
         )

      #Render time of game
      surface.fill((0,0,0), pygame.Rect(
         (settings.VIRTUAL_WIDTH // 2) - 50, 0,
         100,20)
      ) #Rect(x,y,width,height)
      
      render_text(
            surface,
            f"Time: {self.time_in_play}",
            settings.FONTS["score_tiny"],
            settings.VIRTUAL_WIDTH // 2,
            10,
            (255, 255, 255),
            center=True,
        )
      
      

   def on_input(self, input_id: str, input_data: InputData) -> None:
      if input_id == "reset" and input_data.pressed:
         self.state_machine.change("start")
      else:
         self.player.on_input(input_id, input_data)
         #self.all_enemy[0].on_input(input_id, input_data)

   def exit(self) -> None:
        Timer.clear() 
      
