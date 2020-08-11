import pygame
import backend as bk

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (158, 158, 255)

scheme_count = 1

dW = 670
dH = 190

clear_icon = pygame.image.load('icon.png')

cDisplay = pygame.display.set_mode((dW, dH))
pygame.display.set_caption('Live Coronavirus Updates')
pygame.display.set_icon(clear_icon)

clock = pygame.time.Clock()


def text_objects(text, font, c):  # render the text
    text_surface = font.render(text, True, c)
    return text_surface, text_surface.get_rect()


def message_display(text, size, color=(0, 0, 0), coordinates=(dW // 2, dH//2)):
    large_text = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (coordinates[0], coordinates[1])
    cDisplay.blit(text_surf, text_rect)


def print_total(color):
    global cDisplay
    cases, deaths, recoveries = bk.data_return()
    message_display('Global Cases: ' + cases, 40, color, (dW//2, dH//2 - 50))
    message_display('Global Deaths: ' + deaths, 40, color)
    message_display('Global Recoveries: ' + recoveries, 40, color, (dW//2, dH//2 + 50))


def update():
    global light_blue
    global white
    global black
    global scheme_count
    global cDisplay
    scheme_count = 1
    color_back = white
    color_txt = black
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    scheme_count += 1
                    if scheme_count == 4:
                        scheme_count = 1

        if scheme_count == 1:
            color_back = white
            color_txt = black
        elif scheme_count == 2:
            color_back = black
            color_txt = white
        elif scheme_count == 3:
            color_back = light_blue
            color_txt = black

        cDisplay.fill(color_back)
        print_total(color_txt)

        pygame.display.flip()

        clock.tick(60)


update()