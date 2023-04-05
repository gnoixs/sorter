from helpers import *

def main():
    min_n = 5
    max_n = 100
    n = min_n
    slider_pos = HEIGHT + 10

    lst = generate_list(n)

    run = True
    sorting = False
    selected = None
    selected_generator = None

    while run:
        clock.tick(60)
        if sorting:
            try:
                next(selected_generator)
            except StopIteration:
                sorting = False
        else:
            screen.fill(WHITE)
            draw_menu(slider_pos)
            draw_list(lst)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] >= WIDTH - (WIDTH - HEIGHT):
                pos = pygame.mouse.get_pos()
                # selecting algorithm
                if 0 <= pos[1] // (HEIGHT // 11) <= 7 and not sorting:
                    if ALGORITHMS[pos[1] // (HEIGHT // 11)][2] == True:
                        ALGORITHMS[pos[1] // (HEIGHT // 11)][2] = False
                        selected = None
                    else:
                        for algorithm in ALGORITHMS:
                            algorithm[2] = False
                            selected = None
                        ALGORITHMS[pos[1] // (HEIGHT // 11)][2] = True
                        selected = ALGORITHMS[pos[1] // (HEIGHT // 11)][1]
                # changing n size
                elif pos[1] // (HEIGHT // 11) == 8 and not sorting:
                    slider_pos = max(min(pos[0], HEIGHT + 10 + (WIDTH - HEIGHT - 20)), HEIGHT + 10)
                    n = int((slider_pos - HEIGHT - 10) / (WIDTH - HEIGHT - 20) * (max_n - min_n) + min_n)
                    lst = generate_list(n)
                    screen.fill(WHITE)
                    draw_menu(slider_pos)
                    draw_list(lst)
                    pygame.display.update()
                # generating new list
                elif pos[1] // (HEIGHT // 11) == 9 and not sorting:
                    lst = generate_list(n)
                    screen.fill(WHITE)
                    draw_menu(slider_pos)
                    draw_list(lst)
                    pygame.display.update()
                    sorting = False
                # start
                elif pos[1] // (HEIGHT // 11) == 10 and not sorting and selected:
                    sorting = True
                    selected_generator = selected(lst, draw_list, GREEN, RED)

    pygame.quit()

if __name__ == '__main__':
    main()