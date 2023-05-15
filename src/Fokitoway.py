"""
This module was autogenerated by gale.
"""
import pygame
import settings

from gale.game import Game
from gale.input_handler import InputData, InputHandler, InputListener
from gale.state import StateMachine

from src.states import game_states

class Fokitoway(Game, InputListener):
    def init(self) -> None:
        self.state_machine = StateMachine(
            {
                "start": game_states.StartState,
                "play": game_states.PlayState,
                "game-over": game_states.GameOverState,
            }
        )
        self.state_machine.change("start")
        pygame.display.set_icon(settings.TEXTURES["icon_game"])
        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES["background"], (0, 0))
        self.state_machine.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()
        else:
            self.state_machine.on_input(input_id, input_data)
