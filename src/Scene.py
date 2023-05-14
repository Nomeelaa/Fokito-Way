import pygame

import settings


class Scene:
    def __init__(self) -> None:
        self.level = 1
        self.tilemap = {}
        self.items = []
        self.creatures = []
        settings.SceneLoader().load(self, settings.build_scene_path(self.level))

    def render(self, surface: pygame.Surface) -> None:
        for layer in self.tilemap["layers"]:
            for i in range(self.tilemap["rows"]):
                for j in range(self.tilemap["cols"]):
                    surface.blit(
                        settings.TEXTURES["tiles"],
                        layer[i][j]["position"],
                        settings.FRAMES["tiles"][layer[i][j]["frame_index"]],
                    )
