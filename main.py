import random

import pygame, sys

pygame.init()
clock = pygame.time.Clock()


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_change_y
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if ball.y < opponent.y:
        opponent.y -= 7
    if opponent.bottom < ball.bottom:
        opponent.bottom += 7
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_y, ball_speed_x, score_time
    ball.center = (screen_width / 2, screen_height / 2)

    current_time = pygame.time.get_ticks()
    ball_speed_x, ball_speed_y = 0, 0

    if current_time - score_time < 700:
        number_three = game_font.render(f"{3}", False, light_grey)
        screen.blit(number_three, (screen_width / 2 - 5, screen_height / 2 + 30))
    elif current_time - score_time < 1500:
        number_two = game_font.render(f"{2}", False, light_grey)
        screen.blit(number_two, (screen_width / 2 - 5, screen_height / 2 + 30))
    elif current_time - score_time < 2100:
        number_one = game_font.render(f"{1}", False, light_grey)
        screen.blit(number_one, (screen_width / 2 - 5, screen_height / 2 + 30))
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None


# setting up the main window
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pong game")

# Game rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 12, screen_height / 2 - 60, 10, 120)
opponent = pygame.Rect(2, screen_height / 2 - 60, 10, 120)

# colors of players, bg
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_change_y = 0

# score variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

score_time = True

while True:
    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_change_y -= 7
            if event.key == pygame.K_DOWN:
                player_change_y += 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_change_y += 7
            if event.key == pygame.K_DOWN:
                player_change_y -= 7

    screen.fill(bg_color)

    # drawing player, opponent, ball, line and filling colors
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (540, 340))

    player_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(player_text, (450, 340))

    ball_animation()
    player_animation()
    opponent_ai()

    if score_time:
        ball_restart()
        # score_time = None

    # updating the window
    pygame.display.flip()
    clock.tick(60)
