import pygame
from conway import Conway
from cell_sprite import Cell

WHITE = (255, 255, 255)
GREEN = (30, 255, 30)
game_size = 12

if __name__ == "__main__":
    pygame.init()
    pygame.USEREVENT_CONWAY_STEP = pygame.USEREVENT + 1
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode([screen_width, screen_height])

    button_font = pygame.font.SysFont('Arial', 20, True, False)
    start_text = button_font.render("Start", 1, (10, 10, 10))
    start_text_rec = start_text.get_rect()
    start_text_rec.x = 100
    start_text_rec.y = 60

    clear_text = button_font.render("Clear", 1, (10, 10, 10))
    clear_text_rec = clear_text.get_rect()
    clear_text_rec.x = 390
    clear_text_rec.y = 60

    generation_text = button_font.render("Generation: 0", 1, (10, 10, 10))
    generation_text_rec = generation_text.get_rect()
    generation_text_rec.x = 460
    generation_text_rec.y = 400

    cells = pygame.sprite.Group()
    for i in range(game_size):
        for j in range(game_size):
            cells.add(Cell(i, j))

    conway = Conway(game_size)
    clock = pygame.time.Clock()

    done = False
    running = False
    pygame.time.set_timer(pygame.USEREVENT_CONWAY_STEP, 1000)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_text_rec.collidepoint(pos):
                    if running:
                        running = False
                        start_text = button_font.render(
                            "Start", 1, (10, 10, 10))
                    else:
                        running = True
                        start_text = button_font.render(
                            "Stop", 1, (10, 10, 10))
                elif clear_text_rec.collidepoint(pos):
                    for cell in cells:
                        cell.set_live(False)
                    conway.clear()
                    running = False
                    start_text = button_font.render("Start", 1, (10, 10, 10))
                else:
                    for cell in cells:
                        if cell.rect.collidepoint(pos):
                            cell.toggle_live()
                            conway[(cell.col, cell.row)] = int(cell.live)
            elif event.type == pygame.USEREVENT_CONWAY_STEP:
                if running:
                    conway.step()
                    for cell in cells:
                        live = bool(conway.board[(cell.col, cell.row)])
                        cell.set_live(bool(live))

        screen.fill(WHITE)
        generation_text = button_font.render(
            "Generation: {0}".format(conway.generation), 1, (10, 10, 10))

        screen.blit(start_text, start_text_rec)
        screen.blit(clear_text, clear_text_rec)
        screen.blit(generation_text, generation_text_rec)

        cells.draw(screen)
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()
