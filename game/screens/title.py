import pygame
from pygame import mixer

mixer.init()
pygame.init()

mixer.Channel(0).set_volume(0.3)

class TitleScreen:
    screen = pygame.display.set_mode((804, 680))
    clock = pygame.time.Clock()

    mixer.Channel(0).play(mixer.Sound(r"game\sounds\bg_music.mp3"), -1)

    bg_pic = pygame.image.load(r'game\images\bg.png')

    fullscreen = False
    clicking_F11 = False

    while True:
        info = pygame.display.get_window_size()
        bg_pic = pygame.transform.scale(bg_pic, info)

        width, height = info

        font = pygame.font.Font(r'game\fonts\Savior2.ttf', 50*(fullscreen+1))

        title_text = font.render('Leaf Collector', True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(width // 2, height // 3))

        font = pygame.font.Font(r'game\fonts\Savior2.ttf', 33*(fullscreen+1))
        start_text = font.render('Press SPACE to play', True, (0, 0, 0))
        start_rect = start_text.get_rect(center=(width // 2, height // 3*1.5))

        screen.blit(bg_pic, (0, 0))
        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if keys[pygame.K_F11] and fullscreen == False and clicking_F11 == False:
                pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                fullscreen = True
                clicking_F11 = True

            elif keys[pygame.K_F11] and fullscreen and clicking_F11 == False:
                pygame.display.set_mode((804, 680))
                fullscreen = False
                clicking_F11 = True

            if keys[pygame.K_F11] == False:
                clicking_F11 = False

        pygame.display.update()
        clock.tick(120)