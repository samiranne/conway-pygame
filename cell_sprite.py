import pygame


class Cell(pygame.sprite.Sprite):
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)

    def __init__(self, col, row):
        super(Cell, self).__init__()
        self.col = col
        self.row = row
        self.live = False
        self.image = pygame.Surface([25, 25])
        self.image.fill(Cell.GREY)
        self.rect = self.image.get_rect()
        self.rect.x = 100 + 30 * col
        self.rect.y = 100 + 30 * row

    def fill(self):
        color = Cell.BLACK if self.live else Cell.GREY
        self.image.fill(color)

    def toggle_live(self):
        self.live = not self.live
        self.fill()

    def set_live(self, value):
        self.live = value
        self.fill()
