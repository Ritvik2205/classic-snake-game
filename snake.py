import pygame
import random


pygame.init()

''' colours '''
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

'''Sreen size'''
display_height = 700
display_width = 800

'''Initializing display window'''
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake game - Ritvik Gupta")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("comicsans", 25)



def main():

    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_snake = 1

    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Game Over! Press A-Play Again or Q-Quit", red)
            the_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        the_snake(snake_block, snake_list)
        the_score(length_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def the_score(score):
    value = font_style.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

def the_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [display_width / 6, display_height / 3])

if __name__ == "__main__":
    main()
