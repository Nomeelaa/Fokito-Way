"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class IdleState for player.
"""
from gale.input_handler import InputData

#from src.states.player_states.BaseEntityState import BaseEntityState
from src.states.entities.player_states.BaseEntityState import BaseEntityState


class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle")

    def update(self, dt: float) -> None:
        pass
        #self.entity.y += self.entity.vy * dt
        #self.entity.x += self.entity.vx * dt
        #if self.entity.handle_tilemap_collision_on_bottom():
        #    self.entity.vy = 0
        #self.entity.handle_tilemap_collision_on_top()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left" and input_data.pressed:
            self.entity.flipped = True
            self.entity.actual_direction = "left"
            self.entity.change_state("walk", self.entity.actual_direction)
        elif input_id == "move_right" and input_data.pressed:
            self.entity.flipped = False
            self.entity.actual_direction = "right"
            self.entity.change_state("walk", self.entity.actual_direction)

        if input_id == "move_up" and input_data.pressed:
            self.entity.flipped = True
            self.entity.actual_direction = "up"
            self.entity.change_state("walk", self.entity.actual_direction)
        elif input_id == "move_down" and input_data.pressed:
            self.entity.flipped = False
            self.entity.actual_direction = "down"
            self.entity.change_state("walk", self.entity.actual_direction)

        if input_id == "jump" and input_data.pressed:
            self.entity.change_state("jump")
        
        elif input_id == "attack" and input_data.pressed:
            pass
        #    self.entity.change_state("attack")
        
