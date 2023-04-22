import pygame
from game.screens.title import TitleScreen

class Game:
    def __init__(self):
        self.game_start = False
        self.move_right = False
        self.move_left = False
        self.jump = False

        titlescreen = TitleScreen()

        titlescreen.run_title()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.K_SPACE and not self.game_start:
                self.game_start = True

            if event.type == pygame.K_RIGHT:
                self.move_right = True

            if event.type == pygame.K_LEFT:
                self.move_left = True

            if event.type == pygame.K_SPACE and self.game_start:
                self.jump = True