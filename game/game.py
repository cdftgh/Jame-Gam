import pygame
from game.screens.title import TitleScreen

class Game:
    def __init__(self):
        self.game_start = False
        self.move_right = False
        self.move_left = False
        self.jump = False

        self.titlescreen = TitleScreen()

        self.character = pygame.rect.Rect(50, 20, 50, 20)

        self.screen = pygame.display.set_mode(self.titlescreen.get_screen_size())

        self.bg_pic = self.titlescreen.get_bg_pic()

    def handle_events(self):
        self.screen.blit(self.bg_pic, (0, 0))
        self.screen.blit(self.character, (self.screen.get_width() // 2, self.screen.get_height() // 2))

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.K_SPACE and not self.game_start:
                self.game_start = True

            if event.type == pygame.K_RIGHT:
                self.move_right = True

            if event.type == pygame.K_LEFT:
                self.move_left = True

            if event.type == pygame.K_SPACE and self.game_start:
                self.jump = True

            if not keys[pygame.K_RIGHT]:
                self.move_right = False

            if not keys[pygame.K_LEFT]:
                self.move_left = False

        if self.move_right:
            self.character.center += [400]

    def run(self):
        while True:
            if self.game_start:
                self.handle_events()

            elif not self.game_start:
                self.titlescreen.run_title()
