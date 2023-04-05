import random
from globals import *

def generate_list(n):
    lst = []

    for _ in range(n):
        val = random.randint(0, 100)
        lst.append(val)
    
    return lst

def set_list(lst):
    min_val = min(lst)
    max_val = max(lst)
    block_width = (HEIGHT - SIDE_PAD) / len(lst)
    if max_val == min_val:
        block_height = 1    
    else:
        block_height = (HEIGHT - TOP_PAD) / (max_val - min_val)
    start_x = SIDE_PAD // 2

    return {
        'min_val': min_val,
        'max_val': max_val,
        'block_width': block_width,
        'block_height': block_height,
        'start_x': start_x
    }

def draw_menu(slider_pos):
    for algorithm in ALGORITHMS:
        i = ALGORITHMS.index(algorithm)
        if algorithm[2] == True:
            pygame.draw.rect(screen, PASTEL_YELLOW, (HEIGHT, (HEIGHT // 11) * i, WIDTH - HEIGHT, (HEIGHT // 11)))
        else:
            pygame.draw.rect(screen, GREY, (HEIGHT, (HEIGHT // 11) * i, WIDTH - HEIGHT, (HEIGHT // 11)))
        text = font.render(algorithm[0], True, BLACK)
        rect = text.get_rect()
        rect.center = (HEIGHT + (WIDTH - HEIGHT) / 2, (HEIGHT // 11) * i + (HEIGHT // 22))
        screen.blit(text, rect)

    pygame.draw.rect(screen, PASTEL_RED, (HEIGHT, (HEIGHT // 11) * 9, WIDTH - HEIGHT, (HEIGHT // 11)))
    c_text = font.render('Reset', True, BLACK)
    c_rect = c_text.get_rect()
    c_rect.center = (HEIGHT + (WIDTH - HEIGHT) / 2, (HEIGHT // 11) * 9 + (HEIGHT // 22))
    screen.blit(c_text, c_rect)

    pygame.draw.rect(screen, PASTEL_GREEN, (HEIGHT, (HEIGHT // 11) * 10, WIDTH - HEIGHT, (HEIGHT // 11)))
    s_text = font.render('Start', True, BLACK)
    s_rect = s_text.get_rect()
    s_rect.center = (HEIGHT + (WIDTH - HEIGHT) / 2, (HEIGHT // 11) * 10 + (HEIGHT // 22))
    screen.blit(s_text, s_rect)

    pygame.draw.rect(screen, PASTEL_BLUE, (HEIGHT, (HEIGHT // 11) * 8, WIDTH - HEIGHT, (HEIGHT // 11)))
    slider = pygame.draw.rect(screen, GREY, pygame.Rect(HEIGHT + 10, (HEIGHT // 11) * 8 + ((HEIGHT // 11 - 7) / 2), WIDTH - HEIGHT - 20, 7))
    pygame.draw.circle(screen, BLUE, (slider_pos, (HEIGHT // 11) * 8 + ((HEIGHT // 11 - 7) / 2) + 3.5), 7)

def draw_list(lst, color_positions={}, clear_bg=False):
    set_lst = set_list(lst)

    if clear_bg:
        clear_rect = (SIDE_PAD//2, TOP_PAD, HEIGHT - SIDE_PAD, HEIGHT - TOP_PAD)
        pygame.draw.rect(screen, WHITE, clear_rect)
        
    for i, val in enumerate(lst):
        x = set_lst['start_x'] + i * set_lst['block_width']
        y = HEIGHT - (val - set_lst['min_val']) * set_lst['block_height']

        color = GRADIENT[i % 3]

        if i in color_positions:
            color = color_positions[i] 

        pygame.draw.rect(screen, color, (x, y, set_lst['block_width'], HEIGHT))

    if clear_bg:
        pygame.display.update()
