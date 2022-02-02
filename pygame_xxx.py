import pygame
pygame.init()
temp = input("Введите два значения: ")
if len(temp.split()) == 2 and all(map(lambda s: s.isdigit(), temp.split())):
    width, height = map(int, temp.split())
    pygame.display.set_caption(f"{width}x{height}")
    win = pygame.display.set_mode((width, height))
    pygame.draw.line(win, (255, 255, 255), (0, 0), (width, height), width=5)
    pygame.draw.line(win, (255, 255, 255), (0, height), (width, 0), width=5)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.update()
    pygame.quit()
else:
    print("Неправильный тип данных.")
