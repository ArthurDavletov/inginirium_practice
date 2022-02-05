import pygame
pygame.init()


class Circle:
    def __init__(self, x, y, rad, color):
        self.x, self.y = x, y
        self.rad = rad
        self.color = color


class Window:
    def __init__(self):
        self.HEIGHT = 500
        self.WEIGHT = 500
        self.FPS = 120
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.WEIGHT, self.HEIGHT))
        self.circle = Circle(x=self.WEIGHT / 2, y=self.HEIGHT / 2, rad=50, color=(255, 0, 0))
        self.circle_update()

    def circle_update(self):
        self.display.fill((255, 255, 255))
        pygame.draw.circle(self.display, self.circle.color, (self.circle.x, self.circle.y), self.circle.rad)

    def circle_move(self, direction, is_jump=False, dist=1):
        direction = direction.lower()
        if direction == "up":
            self.circle.y -= dist
        elif direction == "right":
            self.circle.x += dist
        elif direction == "down":
            self.circle.y += dist
        elif direction == "left":
            self.circle.x -= dist
        if is_jump:
            self.circle_move(direction=direction, is_jump=False, dist=25)
        self.circle_update()


win = Window()
running = True
motion = "stop"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                motion = "up"
            elif event.key == pygame.K_RIGHT:
                motion = "right"
            elif event.key == pygame.K_DOWN:
                motion = "down"
            elif event.key == pygame.K_LEFT:
                motion = "left"
            elif event.key == pygame.K_END:
                motion = "stop"
            elif event.key == pygame.K_SPACE:
                win.circle_move(motion, is_jump=True)
    if motion in ("up", "right", "down", "left"):
        win.circle_move(motion)

    pygame.display.update()
    win.clock.tick(win.FPS)
