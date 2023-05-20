from typing import TypeVar

from gale.input_handler import InputData

from src.GameEntity import GameEntity
from src.states.entities import player_states

class Player(GameEntity):
    def __init__(self, x: int, y: int, game_level: TypeVar("GameLevel")) -> None:
        self.life = 100
        self.actual_direction = None
        self.attack = 1
        self.weapon = True
        self.victory = False
        super().__init__(
            x,
            y,
            16,
            26,
            "fokito",
            game_level,
            states={
                "idle": lambda sm: player_states.IdleState(self, sm),
                "walk": lambda sm: player_states.WalkState(self, sm),
                "fall": lambda sm: player_states.FallState(self, sm),
                "jump": lambda sm: player_states.JumpState(self, sm),
            },
            animation_defs={
                "idle": {"frames": [0]},
                "idle_horizontal": {"frames": [9]},
                "idle_up": {"frames": [19]},
                "walk_horizontal": {"frames": [9,10,11,12,13,14,15,16,17], "interval": 0.15},
                "walk_up": {"frames": [19,20, 21, 22,23,24,25,26], "interval": 0.15},
                "walk_down": {"frames": [1,2,3,4,5,6,7,8], "interval": 0.15},
                "jump": {"frames": [2]},
            },
            type_player=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.state_machine.on_input(input_id, input_data)
