import pygame

import settings

buttons = []
screen = None
background = None


def init():
    global buttons, screen, background
    screen = pygame.Surface(settings.SIZE)

    name = pygame.image.load('menu_images/name_white.png')
    name = pygame.transform.scale(name, (settings.WIDTH, int(800 * settings.WIDTH / 3840)))
    background = pygame.image.load('backgrounds/menu_background_2.jpg').convert()
    background = pygame.transform.scale(background, settings.SIZE)
    plate = pygame.image.load('menu_images/plate.png').convert_alpha()
    plate = pygame.transform.scale(plate, (500, 500))
    background.blit(name, (0, 0))
    background.blit(plate, (settings.WIDTH // 2 - 250, settings.HEIGHT // 2 - 150))

    play_image = pygame.image.load('menu_images/play_button.png').convert_alpha()
    shop_image = pygame.image.load('menu_images/shop_button.png').convert_alpha()
    exit_image = pygame.image.load('menu_images/exit_button.png').convert_alpha()
    play_image_hover = pygame.image.load('menu_images/play_button_hover.png').convert_alpha()
    shop_image_hover = pygame.image.load('menu_images/shop_button_hover.png').convert_alpha()
    exit_image_hover = pygame.image.load('menu_images/exit_button_hover.png').convert_alpha()
    play_image = pygame.transform.scale(play_image, (400, 100))
    shop_image = pygame.transform.scale(shop_image, (400, 100))
    exit_image = pygame.transform.scale(exit_image, (400, 100))
    play_image_hover = pygame.transform.scale(play_image_hover, (400, 100))
    shop_image_hover = pygame.transform.scale(shop_image_hover, (400, 100))
    exit_image_hover = pygame.transform.scale(exit_image_hover, (400, 100))

    play_button = settings.Button(settings.WIDTH // 2 - 200, settings.HEIGHT // 2 - 100, 400, 100, 'switch_to_levels')
    play_button.image, play_button.image_hover = play_image, play_image_hover
    shop_button = settings.Button(settings.WIDTH // 2 - 200, settings.HEIGHT // 2 + 50, 400, 100, 'switch_to_shop')
    shop_button.image, shop_button.image_hover = shop_image, shop_image_hover
    exit_button = settings.Button(settings.WIDTH // 2 - 200, settings.HEIGHT // 2 + 200, 400, 100, 'exit')
    exit_button.image, exit_button.image_hover = exit_image, exit_image_hover
    buttons += [exit_button, shop_button, play_button]


def create_screen():
    global buttons, screen, background
    screen.blit(background, (0, 0))
    for b in buttons:
        b.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttons:
                b.act(event)
        if event.type == pygame.MOUSEMOTION:
            for b in buttons:
                b.hover_test(event)
    return screen

