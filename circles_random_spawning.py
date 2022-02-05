import pygame
import random
pygame.init()


class Circle:
    def __init__(self):
        self.color = [random.randrange(255), random.randrange(255), random.randrange(255)]


class Window:
    def __init__(self):
        self.WEIGHT, self.HEIGHT = 500, 500
        self.display = pygame.display.set_mode((self.WEIGHT, self.HEIGHT))
        self.display.fill((255, 255, 255))

    def create_new_circle(self):
        pass


if __name__ == "__main__":
    clock = pygame.time.Clock()
    FPS = 120
    clock.tick(FPS)
    win = Window()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        time_counter = clock.tick()
        if time_counter > 3000:
            win.create_new_circle()
            time_counter = 0
        pygame.display.update()
