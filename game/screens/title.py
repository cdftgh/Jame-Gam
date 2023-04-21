import pygame
from pygame import mixer

mixer.init()
pygame.init()

screen = pygame.display.set_mode((804, 680))
clock = pygame.time.Clock()

bg_pic = pygame.image.load(r'game\images\bg.png')

fullscreen = False
clicking_F11 = False

while True:
    info = pygame.display.get_window_size()
    bg_pic = pygame.transform.scale(bg_pic, info)

    screen.blit(bg_pic, (0, 0))

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