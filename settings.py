"""
This module was autogenerated by gale.
"""
from pathlib import Path

import pygame

from gale import frames
from gale import input_handler

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, 'enter')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, 'quit')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, 'move_left')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, 'move_right')

# Size we want to emulate
VIRTUAL_WIDTH = 320
VIRTUAL_HEIGHT = 180

# Size of our actual window
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 720

BASE_DIR = Path(__file__).parent

PLAYER_SPEED = 200

# Register your textures from the graphics folder, for instance:
# TEXTURES = {
#     'my_texture': pygame.image.load(BASE_DIR / "assets" / "graphics" / "my_texture.png")
# }
#
# TEXTURES = {
#     "background": pygame.image.load(BASE_DIR / "graphics" / "background.png"),
#     "spritesheet": pygame.image.load(BASE_DIR / "graphics" / "breakout.png"),
#     "hearts": pygame.image.load(BASE_DIR / "graphics" / "hearts.png"),
#     "arrows": pygame.image.load(BASE_DIR / "graphics" / "arrows.png"),
# }
TEXTURES = {}

# Register your frames, for instance:
# FRAMES = {
#     'my_frames': frames.generate_frames(TEXTURES['my_texture'], 16, 16)
# }
#
# FRAMES = {
#     "paddles": generate_paddle_frames(),
#     "balls": generate_ball_frames(),
#     "bricks": generate_brick_frames(TEXTURES["spritesheet"]),
#     "hearts": generate_frames(TEXTURES["hearts"], 10, 9),
#     "arrows": generate_frames(TEXTURES["arrows"], 24, 24),
# }
FRAMES = {}

pygame.mixer.init()

# Register your sound from the sounds folder, for instance:
# SOUNDS = {
#     'my_sound': pygame.mixer.Sound(BASE_DIR / "assets"  / "sounds" / "my_sound.wav"),
# }
#
# SOUNDS = {
#     "paddle_hit": pygame.mixer.Sound(BASE_DIR / "sounds" / "paddle_hit.wav"),
#     "selected": pygame.mixer.Sound(BASE_DIR / "sounds" / "selected.wav"),
# }
SOUNDS = {}

pygame.font.init()

# Register your fonts from the fonts folder, for instance:
# FONTS = {
#     'small': pygame.font.Font(BASE_DIR / "assets"  / "fonts" / "font.ttf", 8)
# }
FONTS = {
    "tiny": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "fireside.otf", 6),
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "fireside.otf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "fireside.otf", 12),
    "large": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "fireside.otf", 24),
}
