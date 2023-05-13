"""
ISPPJ1 2023
Study Case: Fokito Way

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This module contains all of the states of the FokitoWay game.
"""
from src.states.StartState import StartState
from src.states.GameOverState import GameOverState
from src.states.PlayState import PlayState
from src.states.VictoryState import VictoryState
from src.states.PauseState import PauseState

(
    StartState,
    GameOverState,
    PlayState,
    VictoryState,
    PauseState,
)

#from src.states.HighScoreState import HighScoreState
#from src.states.EnterHighScoreState import EnterHighScoreState
#from src.states.PaddleSelectState import PaddleSelectState
#from src.states.ServeState import ServeState
#(
#    StartState,
#    HighScoreState,
#    EnterHighScoreState,
#    GameOverState,
#    PaddleSelectState,
#    ServeState,
#    PlayState,
#    VictoryState,
#)