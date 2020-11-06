import pygame

pygame.init()
screen_width = 600
screen_height = 600
wn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ninja_Clicker V2")


def play():
    run = True
    play_button = Button()
    while run:
        pygame.display.update()
        wn.fill((20, 20, 20))
        font = pygame.font.SysFont("arial", 50)
        title = font.render("Ninja Clicker", 1, (255, 255, 255))
        wn.blit(title, (screen_width//2 - title.get_width()//2, 150))

        play_button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


class Button(object):
    def __init__(self):
        self.width = 80
        self.height = 30
        self.x = screen_width//2 - self.width//2
        self.y = 250
        self.colour = (0, 0, 0)
        self.font = pygame.font.SysFont("arial", 13)
        self.title = self.font.render("Play Game", 1, (255, 255, 255))

    def update(self):
        pygame.draw.rect(wn, self.colour, (self.x, self.y, self.width, self.height))
        wn.blit(self.title, (self.x + 9, self.y + self.title.get_height()//2))
        self.move()

    def move(self):
        pos = pygame.mouse.get_pos()
        if self.y + self.height + 20 > pos[1] > self.y - 20:
            if self.x + 5 > pos[0] > self.x - 20:
                self.x += 5
            elif self.x + self.width - 5 < pos[0] < self.x + self.width + 20:
                self.x -= 5

        if self.x + self.width + 20 > pos[0] > self.x - 20:
            if self.y + 5 > pos[1] > self.y - 20:
                self.y += 5
            if self.y + self.height - 5 < pos[1] < self.y + self.height + 20:
                self.y -= 5

play()
