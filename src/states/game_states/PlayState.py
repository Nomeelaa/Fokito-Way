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

      for _ in range(randint(3,30)):
         self.all_enemy.append(Enemy(randint(18,100), randint(50,400), self.game_level))

      if (self.player.life == 100):
         print("Life of player: 100")

      for _, enemy in enumerate(self.all_enemy):
         enemy.change_state("idle", randint(1,10))
    

      def create_new_enemy():
         for _ in range(randint(1,10)):
            self.all_enemy.append(Enemy(randint(18,100), randint(50,400), self.game_level))
         #for _, enemy in enumerate(self.all_enemy):
         #   enemy.change_state("idle", randint(1,10)) #reset all enemy time

      #Timer.every(30, create_new_enemy, 2)

      self.time_in_play = "00:00"
      #self.time_in_play = "00:00:00"
      self.timer = 0
      self.seconds = 0
      self.minutes = 0
      self.hours = 0

      def count_timer():
         self.seconds += 1
         #for _, enemy in enumerate(self.all_enemy):
         #   enemy.timer += 1
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

      #self.enemy.update(dt)

      for _, enemy in enumerate(self.all_enemy):
         enemy.update(dt, self.seconds)
         #print(f"enemy({_})")
      
      #print(self.seconds)
      #print("seconds: ", self.all_enemy[0].seconds)
      #print("minutes: ",self.all_enemy[0].min)
      #print("hours: ",self.all_enemy[0].hrs)

      #for i in range(4):
      #   self.all_enemy[i].update(dt)


      #self.enemy.update(dt)
      #self.enemy.solve_world_boundaries()
      self.game_level.update(dt)
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

               #self.all_enemy[i].vx = 0
               #self.all_enemy[i].vy = 0
               #self.all_enemy[i].change_animation("idle")
      else:
         self.state_machine.change("game_over", score=self.score)
      #for i in range(len(self.all_enemy)):
      #for i in range(4):
      #   if self.all_enemy[i].collides(self.player):
      #      print("score: ", self.score)
      #      if (self.player.weapon is None):
      #         self.player.life -= 1
      #      else:
      #         self.all_enemy[i].life -= self.player.attack
      #      if self.all_enemy[i].life == 0:
      #         self.all_enemy.remove(self.all_enemy[i])
      #         break
      #      if (self.player.life == 0):
      #         self.state_machine.change("game_over", score=self.score)
      #         break
      #   if self.player.collides(self.all_enemy[i]):
      #      print("Colision")

      #      self.all_enemy[i].vx = 0
      #      self.all_enemy[i].vy = 0
      #      self.all_enemy[i].change_animation("idle")
      

   def render(self, surface: pygame.Surface) -> None:
      surface.fill((0,0,0))

      world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
      self.game_level.render(world_surface)
      

      
      
      self.player.render(world_surface)
      #self.enemy.render(world_surface)

      for _, enemy in enumerate(self.all_enemy):
         enemy.render(world_surface)

      #for i in range(4):
      #   self.all_enemy[i].render(world_surface)
      #self.enemy.render(surface)
      surface.blit(world_surface, (-self.camera.x, -self.camera.y))

      render_text(
         surface,
         "Life",
         settings.FONTS["score_tiny"],
         470,
         5,
         (255, 255, 255),
      )

      surface.fill((255,255,255), pygame.Rect(520,2,104,14)) #Rect(x,y,width,height)
      surface.fill((0,0,0), pygame.Rect(522,4,100,10)) #Rect(x,y,width,height)
      surface.fill((255,0,0), pygame.Rect(522,4,self.player.life,10)) #Rect(x,y,width,height)
      
      render_text(
         surface,
         f"Score: {self.score}",
         settings.FONTS["score_tiny"],
         settings.VIRTUAL_WIDTH - 80,
         20,
         (255, 255, 255),
      )

      
      render_text(
         surface,
         f"Time: {self.time_in_play}",
         settings.FONTS["score_tiny"],
         settings.VIRTUAL_WIDTH - 150,
         55,
         (255, 255, 255),
         shadowed=True,
      )
      

   def on_input(self, input_id: str, input_data: InputData) -> None:
      self.player.on_input(input_id, input_data)
      self.all_enemy[0].on_input(input_id, input_data)

   def exit(self) -> None:
        Timer.clear() 
      
