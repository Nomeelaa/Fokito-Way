""" 
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Start state.
"""
from typing import Any, Dict, Tuple

import sys
import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings


class GameOverState(BaseState):
    def enter(self, **enter_params: dict) -> None:
      self.selected = 1
      self.score = enter_params.get("score", 0)

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((0,0,0))

        render_text(
            surface,
            "Game Over",
            settings.FONTS["large"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 3,
            (255, 255, 255),
            center=True,
        )

        color = (52, 235, 216) if self.selected == 1 else (255, 255, 255)

        render_text(
            surface,
            "Play Again",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 60,
            color,
            center=True,
        )

        color = (52, 235, 216) if self.selected == 2 else (255, 255, 255)

        render_text(
            surface,
            "Close Game",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 30,
            color,
            center=True,
        )
      
        print("score: ", self.score)
        render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["score_tiny"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_down" and input_data.pressed and self.selected == 1:
            #settings.SOUNDS["paddle_hit"].play()
            self.selected = 2
        elif input_id == "move_up" and input_data.pressed and self.selected == 2:
            #settings.SOUNDS["paddle_hit"].play()
            self.selected = 1
        elif input_id == "enter" and input_data.pressed:
            #settings.SOUNDS["selected"].play()
            pass

            if self.selected == 1:
                self.state_machine.change("play", level=1)
                #self.state_machine.change("play", level=1, player=self.player, enemy=self.enemy)
            else:
                sys.exit()