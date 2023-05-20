""" 
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Start state.
"""
import pygame
import sys
import random


from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings


class StartState(BaseState):
    def enter(self) -> None:
        self.level = 1
        self.score = 0
        self.selected = 1

    def update(self, dt: float) -> None:
        pass

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

        if input_id == "change" and input_data.pressed:
            self.state_machine.change("victory", level=self.level, score=self.score, state="END")

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            "Fokito Way",
            settings.FONTS["large"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 3,
            (255, 255, 255),
            center=True,
        )

        color = (52, 235, 216) if self.selected == 1 else (255, 255, 255)

        render_text(
            surface,
            "Play Game",
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
